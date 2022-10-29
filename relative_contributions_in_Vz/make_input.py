import sys
import os
from pathlib import Path
import subprocess
from mendeleev import element

path_mrchem_gui = '/home/ambr/software/mrchem-gui/input_generator'
sys.path.append(path_mrchem_gui)

from mrchem_input_templates import EnergyCalculation, EnergyZORACalculation
from mrchem_input_generator import Molecule

bools = (True, False)
combinations = [(has_nuc, has_coul, has_xc) for has_nuc in bools for has_coul in bools for has_xc in bools]
nobilities = ('He', 'Ne', 'Ar', 'Kr', 'Xe')

calc_dir = Path.cwd().joinpath('calcs')

for combo in combinations:
    has_nuc, has_coul, has_xc = combo
    if not any(combo):
        continue
    for noble in nobilities:

        # GENERATE INPUT FILES
        mol = Molecule.from_string(f'{noble} 0.0 0.0 0.0')
        i = EnergyZORACalculation(molecule=mol)
        i.input.world_prec = 1e-6
        i.input.SCF.orbital_thrs = 1e-5
        i.input.SCF.guess_type = 'sad_gto'
        i.input.SCF.guess_prec = 1e-5
        i.input.SCF.localize = True
        i.input.ZORA.include_nuclear = has_nuc
        i.input.ZORA.include_coulomb = has_coul
        i.input.ZORA.include_xc = has_xc
        i.input.WaveFunction.method = 'pbe'

        i.fname = calc_dir.joinpath(f'{noble}_{int(has_nuc)}{int(has_coul)}{int(has_xc)}.inp')
        i.write()

# NREL calculations
for noble in nobilities:
    mol = Molecule.from_string(f'{noble} 0.0 0.0 0.0')
    i = EnergyCalculation(molecule=mol)
    i.input.world_prec = 1e-6
    i.input.SCF.orbital_thrs = 1e-5
    i.input.SCF.guess_type = 'sad_gto'
    i.input.SCF.guess_prec = 1e-5
    i.input.SCF.localize = True
    i.input.WaveFunction.method = 'pbe'

    i.fname = calc_dir.joinpath(f'{noble}_nrel.inp')
    i.write()

