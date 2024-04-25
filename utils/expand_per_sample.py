"""
Expand the given input .npy file into 1000 .nii.gz files, each containing one slice (sample) of the original file.

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 4/25/2024
"""
# %%
import numpy as np
from prepare_data_from_nnUNet import resample_npy_to_nii

# Load the .npy file
path = "../data/whole-heart-ultrasound-64-1000samples-hearts1-30.npy"

arr = np.load(path)
print(arr.shape)

# %%
split_arr = np.split(arr, 1000, axis=0)
print(len(split_arr))
print(split_arr[0].shape)

# %%
# Save each array to a separate file
for i, arr in enumerate(split_arr):
    resample_npy_to_nii(arr, f"../data/samples/sample_{i}.nii.gz", f"../data/synthetic_hearts/imagesTr/sample_{i}_resampled.nii.gz")

# %%
