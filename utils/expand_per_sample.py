"""
Expand the given input .npy file into 1000 .nii.gz files, each containing one slice (sample) of the original file.

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 4/25/2024
"""
# %%
import numpy as np
import nibabel as nib
import os

print(os.getcwd())

def npy_to_nii(
    input_arr: np.ndarray,
    output_path: str,
):
    """
    Save .npy as .nii.gz file.

    Parameters:
    - input_path: Input .npy file (This needs to be in image, not point cloud format)
    - output_path: Path to save the .nii.gz file.
    """
    # Load the NumPy array
    new_image = nib.Nifti2Image(input_arr, affine=np.eye(4))
    nib.save(new_image, output_path)

# Load the .npy file
# path = "../data/whole-heart-segmentations-wh-128-1000samples-hearts1-30.npy"
path = "../data/whole-heart-ultrasound-128-1000samples-hearts1-30.npy"

arr = np.load(path)
print(arr.shape)

# %%
split_arr = np.split(arr, 1000, axis=0)
print(len(split_arr))
print(split_arr[0].shape)

# %%
# Save each array to a separate file
for i, arr in enumerate(split_arr):
    # npy_to_nii(arr, f"../data/synthetic_hearts/labelsTr/segmentation_{i}.nii.gz")
    npy_to_nii(arr, f"../data/synthetic_hearts/imagesTr/sample_{i}_0000.nii.gz")

# %%
