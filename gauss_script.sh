#!/bin/bash
#SBATCH --export=ALL
#SBATCH --partition=teaching
#SBATCH --account=teaching
#SBATCH --distribution=cyclic
#SBATCH --ntasks=4 --nodes=1
#SBATCH --time=01:00:00
#SBATCH --job-name=gauss_2cores
#SBATCH --output=slurm-%j.out
module purge
module load gaussian/g16
/opt/software/scripts/job_prologue.sh
export GAUSS_SCRDIR=$SLURM_SUBMIT_DIR
g16 < Molecule_ANTCEN.com > Molecule_ANTCEN.log
g16 < Molecule_PENCEN.com > Molecule_PENCEN.log
g16 < Molecule_TETCEN.com > Molecule_TETCEN.log
/opt/software/scripts/job_epilogue.sh
