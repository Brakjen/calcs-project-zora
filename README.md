# Folder Overview

## reaction_energies
This folder stores the input and output files for some transition metal-ligand interaction energies. Data analysis done in `ReactionEnergiesAnalysis.ipynb`.

## row5
This folder stores input and output files for MW and GTO calculations on all the row 5 elements. Multiple MW precisions tested, and different integration grids for GTO also tested (defgrid 2 vs defgrid3). Jupyter notebooks contain different kinds of analyses and comparisons between MW and GTO.

## small_molecules
This folder stores input and output files for some small row 5 hydrides, fuorides and oxides, as well as iodide. Analysis in `SmallMoleculeAnalysis.ipynb`.

## relative_contributions_in_Vz
This folder contains the study of how the different contributions of the ZORA potential interacted together (the additivity). Analysis in `analysis/RelativeContributionsAnalysis.ipynb`.

## implementation-tests
This folder contains some older implementation test. Input file generation script not available. The analysis is done in the notebooks.

## old
This folder contains some tests from the early stages of the implementation. Not really documented, but some sense can probably be deduced from the code, notebooks and figures.

# Scripts
List of the most important scripts I have used
- Input file generation: https://github.com/MRChemSoft/mrchem-gui
- SLURM file generation: https://github.com/Andersmb/PySlurm
- SLURM Queue GUI: https://github.com/Andersmb/QView
