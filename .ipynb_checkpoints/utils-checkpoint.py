import os


def read_xyz(xyzfile):
    with open(xyzfile) as f:
        lines = f.readlines()[2:]
    return [' '.join(line.split()) for line in lines]


def get_speeds(n=8):
    c = 137.035989
    cs = [c / 4, c / 2, c, 2 * c, 4 * c, 8 * c, 16 * c, 32 * c]
    return cs


def input_orca(charge=None, mult=None, xyzfile=None, c=None, basis=None, nprocs=None, zora=False):
    i = []
    i.append(f'! LDA {basis} nori grid5 finalgrid6 verytightscf')
    if nprocs is not None:
        i.append(f'%Pal NProcs {nprocs} End')
    if zora:
        i.append('')
        i.append('% REL')
        i.append('  Method ZORA')
        i.append('  ModelPot 1, 0, 0, 0')
        i.append(f'  velit {c}')
        i.append('END')
    i.append('')
    i.append(f'*xyz {charge} {mult}')
    for atom in read_xyz(xyzfile):
        i.append(atom)
    i.append('*')
    return i


def input_mrchem(charge=None, mult=None, xyzfile=None, c=None,
                 initorb=None, writeorb=True, world_prec=None,
                 guess_prec=None, zora=False, guess_type='sad_dz'):
    i = []
    i.append(f'world_prec = {world_prec}')
    i.append(f'world_size = 5')
    i.append('world_unit = angstrom')
    i.append('')
    i.append('Molecule {')
    i.append(f'  charge = {charge}')
    i.append(f'  multiplicity = {mult}')
    i.append(f'  $coords')
    for atom in read_xyz(xyzfile):
        i.append('  ' + atom)
    i.append('  $end')
    i.append('}')
    i.append(' WaveFunction {')
    i.append(f'  method = LDA')
    i.append(f'  zora = {str(zora).lower()}')
    i.append('}')
    if zora:
        i.append('ZORA {')
        i.append(f'  light_speed = {c}')
        i.append('}')
    i.append('SCF {')
    if guess_prec is not None:
        i.append(f'  guess_prec = {guess_prec}')
    i.append(f'  guess_type = {guess_type}')
    i.append('  max_iter = 100')
    i.append('  kain = 10')
    i.append(f'  energy_thrs = {world_prec}')
    i.append(f'  orbital_thrs = {world_prec * 10}')
    i.append('  localize = true')
    i.append(f'  write_orbitals = {str(writeorb).lower()}')
    i.append('}')
    if initorb is not None:
        i.append('Files {')
        i.append(f'  guess_phi_p = \'{initorb}\'')
        i.append('}')
    i.append('Derivatives {')
    i.append('  zora = abgv_00')
    i.append('}')
    return i


def energy_orca(outfile):
    with open(outfile) as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().startswith('FINAL SINGLE POINT ENERGY'):
            return float(line.strip().split()[4])