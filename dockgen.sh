#! /bin/bash
source /opt/anaconda/etc/profile.d/conda.sh
conda activate diffdock
export LD_LIBRARY_PATH=/opt/anaconda/envs/diffdock/lib:$LD_PATH
python protein_ligand_csv_generation.py --path DockGen/processed_files --out test_dockgen.csv 
python -m inference --protein_ligand_csv test_dockgen.csv --out_dir results/dockgen --inference_steps 20 --samples_per_complex 40 --batch_size 10 --actual_steps 18 --no_final_step_noise --precomputed_dir /opt/data/private/diffdock-v1/DiffDock/cache/dockgen_embeddings.pkl
python evaluate_files.py --results_path results/dockgen --num_predictions 40 --data_dir data/DockGen/processed_files --test_names_path data/DockGen/split_test.txt