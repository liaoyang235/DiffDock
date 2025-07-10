#! /bin/bash
source /opt/anaconda/etc/profile.d/conda.sh
conda activate diffdock
export LD_LIBRARY_PATH=/opt/anaconda/envs/diffdock/lib:$LD_PATH
python protein_ligand_csv_generation.py --path posebusters_paper_data/posebusters_benchmark_set --out test_posebusters.csv 
python -m inference --protein_ligand_csv test_posbusters.csv --out_dir results/posebusters --inference_steps 20 --samples_per_complex 40 --batch_size 10 --actual_steps 18 --no_final_step_noise --precomputed_dir cache/posebusters_embeddings.pkl
python evaluate_files.py --results_path results/posebusters --num_predictions 40 --data_dir posebusters_paper_data/posebusters_benchmark_set --test_names_path posebusters_paper_data/posebusters_benchmark_set_ids.txt