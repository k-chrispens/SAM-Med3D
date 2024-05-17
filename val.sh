python validation.py --seed 2023\
 -vp ./results/exp_fine_tuned_db \
 -cp ./work_dir/fine_tune_experimental_augmented/sam_model_6_step_dice:0.9039047360420227_best.pth \
 -tdp ./data/validation/experimental/ -nc 1 \
 --save_name ./results/sam_med3d_exp_db.py
#  -cp ./work_dir/fine_tune_experimental_augmented/sam_model_latest.pth \
