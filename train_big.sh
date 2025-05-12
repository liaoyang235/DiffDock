#! /bin/bash

source /opt/anaconda/etc/profile.d/conda.sh
conda activate diffdock
export LD_LIBRARY_PATH=/opt/anaconda/envs/diffdock/lib:$LD_PATH
export WANDB_API_KEY=03f3de19782b6a3424a5f4521bb30fd98f4b25fa
wandb login
cd /opt/data/private/DiffDock
python3 train.py --pdbbind_esm_embeddings_path data/PDBBind_sequences.pt --run_name without_DTR --wandb --batch_size 16 --no_batch_norm --num_conv_layers 5 --n_epochs 850 --limit_complexes 10000 --ns 48 --nv 10 --atom_max_neighbors 24 --dropout 0.1