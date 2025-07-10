#! /bin/bash
source /opt/anaconda/etc/profile.d/conda.sh
conda activate diffdock
export LD_LIBRARY_PATH=/opt/anaconda/envs/diffdock/lib:$LD_PATH
python protein_ligand_csv_generation.py --path posebusters_paper_data/astex_diverse_set --out test_astex.csv 
python -m inference --protein_ligand_csv test_astex.csv --out_dir results/astex --inference_steps 20 --samples_per_complex 40 --batch_size 10 --actual_steps 18 --no_final_step_noise --precomputed_dir cache/astex_embeddings.pkl
python evaluate_files.py --results_path results/astex --num_predictions 40 --data_dir posebusters_paper_data/astex_diverse_set --test_names_path posebusters_paper_data/astex_diverse_set_ids.txt