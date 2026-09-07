#!/bin/bash

#SBATCH --account=education-eemcs-courses-tw3740tu
#SBATCH --job-name=MonteCarlo
#SBATCH --partition=compute
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=12
#SBATCH --mem=4G
#SBATCH --time=00:30:00
#SBATCH --output=monte_carlo_%j.out

srun python3 monte_carlo.py