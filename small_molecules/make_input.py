import sys
import os
from pathlib import Path
import subprocess

path_mrchem_gui = '/cluster/home/ambr/software/mrchem-gui/input_generator'
sys.path.append(path_mrchem_gui)

from mrchem_input_templates import EnergyCalculation, EnergyZORACalculation
from mrchem_input_generator import Molecule

calc_dir = Path.cwd().joinpath('calcs')
xyz_dir = Path.cwd().joinpath('xyz_files')

prec = 1e-5

for xyz in xyz_dir.glob('*.xyz'):
    # GENERATE INPUT FILES
    mol = Molecule.from_xyzfile(xyz)
    i = EnergyZORACalculation(molecule=mol, include_xc=False, include_coulomb=False)
    i.input.world_prec = prec
    i.input.world_unit = 'angstrom'
    i.input.SCF.orbital_thrs = prec * 10
    i.input.SCF.guess_type = 'sad_gto'
    i.input.SCF.guess_prec = prec
    i.input.SCF.localize = True
    i.input.SCF.kain = 6
    i.input.SCF.max_iter = 500
    i.input.SCF.write_orbitals = True
    i.input.WaveFunction.method = 'pbe'

    if mol.multiplicity > 1:
        i.input.WaveFunction.restricted = False

    i.fname = calc_dir.joinpath(calc_dir.joinpath(xyz.stem + '.inp'))
    i.write()

