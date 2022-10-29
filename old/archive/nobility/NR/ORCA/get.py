import pandas as pd
from glob import glob


def energy(outfile):
    with open(outfile) as f:
        lines = f.readlines()
    for line in lines:
        if line.strip().startswith('FINAL SINGLE POINT ENERGY'):
            return float(line.strip().split()[4])


files = glob('*.out')

table = []
for f in files:
    atom, basis, ext = f.split('_')
    e = energy(f)
    row = (atom, basis, e)
    table.append(row)

df = pd.DataFrame(table, columns=['Atom', 'BasisSet', 'Energy'])
df.to_csv('NR_ORCA.csv', index=False)
