import sys
import os
from pathlib import Path
import subprocess

path_mrchem_gui = '/cluster/home/ambr/software/mrchem-gui/input_generator'
sys.path.append(path_mrchem_gui)

from mrchem_input_templates import EnergyCalculation, EnergyZORACalculation
from mrchem_input_generator import Molecule

calc_dir = Path.cwd().joinpath('calcs_nrel')  #                          <<<
xyz_dir = Path.cwd().joinpath('xyz_files')

prec = 1e-6

for xyz in xyz_dir.glob('*.xyz'):
    # GENERATE INPUT FILES
    mol = Molecule.from_xyzfile(xyz)
    i = EnergyCalculation(molecule=mol)  #                           <<<
    i.input.world_prec = prec
    i.input.world_size = 6
    i.input.world_unit = 'angstrom'
    i.input.SCF.orbital_thrs = prec * 50
    i.input.SCF.guess_type = 'sad_gto' #                             <<<
    i.input.SCF.guess_prec = prec
    i.input.SCF.localize = True
    i.input.SCF.kain = 6
    i.input.SCF.max_iter = 500
    i.input.SCF.write_orbitals = True
    i.input.WaveFunction.method = 'pbe'
    # i.input.WaveFunction.relativity = 'zora'  #                          <<<

    if mol.multiplicity > 1:
        i.input.WaveFunction.restricted = False

    fname = calc_dir.joinpath(xyz.stem + '_mw6' + '.inp')
    print(fname)
    i.fname = calc_dir.joinpath(fname)
    i.write()

