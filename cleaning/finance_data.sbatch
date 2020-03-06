#!/bin/bash
#SBATCH -J 10k
#SBATCH -o 10k_clean_%A-%a.out
#SBATCH --array=0-59              
#SBATCH -p htc
#SBATCH --mem=6G
#SBATCH --cpus-per-task=1

# Load Python3
module purge
module load python

data_dir="/users/egodat/workshops/data/finance_10k/data10k/"
readarray files < <(ls ${data_dir}*txt)
f=${files[${SLURM_ARRAY_TASK_ID}]}

export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
python3 data_clean.py ${f}
