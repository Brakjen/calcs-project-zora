import matplotlib
from matplotlib.ticker import LogLocator, NullFormatter
import matplotlib.pyplot as plt
import sys
import numpy as np
from pathlib import Path


def getEnergies(lines):
    return [float(line.split()[2]) for line in lines if line.strip().startswith('Total energy') and ":" not in line]

def getThresholds(lines):
    try:
        e = [float(line.split()[3]) for line in lines if line.strip().startswith('Energy threshold')][0]
    except ValueError:
        e = None
    try:
        o = [float(line.split()[3]) for line in lines if line.strip().startswith('Orbital threshold') and ":" in line][0]
    except ValueError:
        o = None

    return e, o

def getResiduals(lines):
    return [abs(float(line.split()[2])) for line in lines if line.strip().startswith('Total residual')]

def getUpdates(lines):
    return [abs(float(line.split()[3])) for line in lines if line.strip().startswith('Total energy') and ":" not in line]

def plot(f, savefig=False):
    jobname = Path(f).absolute()

    with open(f) as file:
        lines = file.readlines()

    energies = getEnergies(lines)
    updates = getUpdates(lines)
    residuals = getResiduals(lines)
    e, o = getThresholds(lines)
    xs = [i for i in range(len(energies))]

    maxu, minu = max(updates), min(updates)
    maxr, minr = max(residuals), min(residuals)

    ymax = 10**np.ceil(np.log10(max((maxu, maxr))))
    ymin = 10**np.floor(np.log10(min((minu, minr))))
    ratio = np.ceil(ymax // ymin)

    fig, ax = plt.subplots(figsize=(6, 4), dpi=150)
    ax.set_yscale('log')
    ax.yaxis.set_major_locator(LogLocator(base=10, numticks=ratio))
    ax.yaxis.set_minor_locator(LogLocator(base=10, subs=np.arange(1.0, 10.0)*0.1, numticks=10))
    ax.yaxis.set_minor_formatter(NullFormatter())

    ax.set_xlabel('SCF Iteration')
    ax.set_ylabel('Atomic Units')
    ax.set_title(f'MRChem convergence for {jobname.name}', y=1.15)

    if e is not None:
        ax.axhline(e, color='skyblue', lw=1, ls='--')
    if o is not None:
        ax.axhline(o, color='salmon', lw=1, ls='--')

    pu = ax.plot(xs, updates, marker='.', mec='black', color='skyblue', lw=1, ls='-', label='Energy Update')
    pr = ax.plot(xs, residuals, marker='.', mec='black', color='crimson', lw=1, ls='-', label='Total Residual')

    ax2 = ax.twinx()
    ax2.set_ylabel('Total Energy (a.u.)')
    ax2.ticklabel_format(useOffset=False)
    pe = ax2.plot(xs, energies, color='black', lw=1, ls='--', marker='.', mfc='white', label='Total Energy')

    plots = pu + pr + pe
    labels = [p.get_label() for p in plots]

    ax.legend(labels=labels, handles=plots, loc='lower center', bbox_to_anchor=(0.5, 1.0), ncol=3)

    ax.grid(ls=':', lw=0.5, color='gray')
    fig.tight_layout()
    
    if savefig:
        fig.savefig(Path('').joinpath(jobname.stem + '.png'))
    else:
        fig.show()


if __name__ == '__main__':
    f = sys.argv[1]
    plot(f, savefig=True)