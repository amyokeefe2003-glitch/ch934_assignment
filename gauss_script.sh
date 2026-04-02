#!/bin/bash
#SBATCH --export=ALL
#SBATCH --partition=teaching
#SBATCH --account=teaching
#SBATCH --distribution=cyclic
#SBATCH --ntasks=8 --nodes=1
#SBATCH --time=01:00:00
#SBATCH --job-name=gauss_8cores
#SBATCH --output=slurm-%j.out
module purge
module load gaussian/g16
/opt/software/scripts/job_prologue.sh
export GAUSS_SCRDIR=$SLURM_SUBMIT_DIR
g16 < Molecule_ANTCEN.com > Molecule_ANTCEN_8cores.log
g16 < Molecule_PENCEN.com > Molecule_PENCEN_8cores.log
g16 < Molecule_TETCEN.com > Molecule_TETCEN_8cores.log
/opt/software/scripts/job_epilogue.sh
