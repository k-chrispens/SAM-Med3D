"""
Convert dataset of .npy files to .nii.gz files.

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 4/30/2024
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
    new_image = nib.Nifti2Image(input_arr, affine=np.eye(4))
    nib.save(new_image, output_path)

# Load the .npy files
path_img = "../data/experimental_hearts/ultrasound"
path_label = "../data/experimental_hearts/segmentations"

# %%
files_img = os.listdir(path_img)
files_label = os.listdir(path_label)
print(files_img)
print(files_label)

# %%
# Save each array to a separate file
for i, (img_file, label_file) in enumerate(zip(files_img, files_label)):
    arr_img = np.load(os.path.join(path_img, img_file))
    arr_label = np.load(os.path.join(path_label, label_file))
    npy_to_nii(arr_img, f"../data/experimental_hearts/sample_{i}_0000.nii.gz")
    npy_to_nii(arr_label, f"../data/experimental_hearts/sample_{i}.nii.gz")

# %%
