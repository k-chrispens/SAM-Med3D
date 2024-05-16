"""
Convert a volume sequence into .nii.gz files, for use in inference (meaning that corresponding empty masks are also generated).

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 5/14/2024
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

# Load the files
path_img = "../data/inference/ultrasound"
path_label = "../data/inference/segmentations"

# %%
img = np.load(os.path.join(path_img, "2023-11-21_US12.npy"))
label = np.load(os.path.join(path_label, "mask.npy"))

# %%
# Save each frame volume to a separate file
for i in range(0, img.shape[0]):
    npy_to_nii(img[i], f"../data/inference/sample_{i}_0000.nii.gz")
    npy_to_nii(label, f"../data/inference/sample_{i}.nii.gz")

# %%
