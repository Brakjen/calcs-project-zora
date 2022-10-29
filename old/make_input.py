import os
from utils import *

root = '/Users/abr121/Documents/dev/proj_zora'
dir_mrchem = os.path.join(root, 'inputfiles', 'mrchem')
dir_orca = os.path.join(root, 'inputfiles', 'orca')
dir_xyz = os.path.join(root, 'XYZfiles')

molecules = ['CO2', 'H2O', 'PH2OH', 'CH3BH2', 'CrCO6']
c = 137.035989
basis_sets = [
    'def2-svp',
    'def2-tzvp',
    'def2-qzvpp',
    'zora-def2-svp',
    'zora-def2-tzvp',
    'zora-def2-qzvpp',
    'pc-1',
    'pc-2',
    'pc-3',
    'pc-4',
    'ano-rcc-dzp',
    'ano-rcc-tzp',
    'ano-rcc-qzp',
    'cc-pcvdz',
    'cc-pcvtz',
    'cc-pcvqz',
    'cc-pcv5z',
    'cc-pvdz',
    'cc-pvtz',
    'cc-pvqz',
    'cc-pv5z'
]

charge = 0
mult = 1
world_prec = 1e-7
guess_prec = 1e-5
zora = True
initorb = '../../../initorbs'
guess_type = 'mw'
write_orbitals = False

params_m = {
    'charge': charge,
    'mult': mult,
    'zora': zora,
    'initorb': initorb,
    'world_prec': world_prec,
    'guess_type': guess_type,
    'guess_prec': guess_prec,
    'writeorb': write_orbitals
}
params_o = {
    'mult': mult,
    'zora': True,
    'nprocs': 18
}

for mol in molecules:
    for basis in basis_sets:
        fname = f'{mol}_{basis}_'
        i = input_orca(charge=charge,
                       xyzfile=os.path.join(dir_xyz, f'{mol}.xyz'),
                       basis=basis,
                       c=c,
                       **params_o)
        with open(os.path.join(dir_orca, fname+'.inp'), 'w') as f:
            f.write('\n'.join(i))