cd /media/liao/portable_ntfs/DiffDock
source /mnt/ubuntu/anaconda3/etc/profile.d/conda.sh
conda activate diffdock
python3 evaluate_with_DTR.py --run_name DTR_0.8_eval_no_limit --wandb --dataset pdbbind --data_dir data/PDBBind_processed/ --split_path \
                data/splits/timesplit_no_lig_overlap_val --esm_embeddings_path data/PDBBind_sequences.pt \
                --samples_per_complex 10 --model_dir workdir/test_score/DTR_0.8_wo_for_eval --batch_size 10 \
                --specific_model epoch_69_model.pt
python3 evaluate_with_DTR.py --run_name DTR_0.8_eval_no_limit --wandb --dataset pdbbind --data_dir data/PDBBind_processed/ --split_path \
                data/splits/timesplit_no_lig_overlap_val --esm_embeddings_path data/PDBBind_sequences.pt \
                --samples_per_complex 10 --model_dir workdir/test_score/DTR_0.8_wo_for_eval --batch_size 10 \
                --specific_model epoch_79_model.pt
python3 evaluate_with_DTR.py --run_name DTR_0.8_eval_no_limit --wandb --dataset pdbbind --data_dir data/PDBBind_processed/ --split_path \
                data/splits/timesplit_no_lig_overlap_val --esm_embeddings_path data/PDBBind_sequences.pt \
                --samples_per_complex 10 --model_dir workdir/test_score/DTR_0.8_wo_for_eval --batch_size 10 \
                --specific_model epoch_89_model.pt