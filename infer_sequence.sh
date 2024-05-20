python infer_sequence.py --seed 2023 \
 -tdp ./data/inference/no_spaced -nc 1 \
 -cp ./work_dir/fine_tune_exp_aug_no_spaced/sam_model_dice_best.pth \
 --output_dir ./results/  \
 --task_name sequence_exp_no_spaced
