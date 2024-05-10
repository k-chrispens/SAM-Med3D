"""
Convert dataset of .npy files to .nii.gz files.

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 4/30/2024
"""
# %%
import numpy as np
import nibabel as nib
import os
import SimpleITK as sitk

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

def seg_nrrd_to_nii(
    input_path: str,
    output_path: str,
):
    """
    Save .nrrd as .nii.gz file.

    Parameters:
    - input_path: Input .nrrd file (This needs to be in image, not point cloud format)
    - output_path: Path to save the .nii.gz file.
    """
    img = sitk.ReadImage(input_path)
    sitk.WriteImage(img, output_path)

# Load the files
path_img = "../data/validation/experimental/img"
path_label = "../data/validation/experimental/label"

# %%
files_img = os.listdir(path_img)
files_label = os.listdir(path_label)
files_img.sort()
files_label.sort()
print(files_img)
print(files_label)

# %%
# Save each array to a separate file
for i, (img_file, label_file) in enumerate(zip(files_img, files_label)):
    print(img_file, label_file)
    if os.path.splitext(img_file)[1] == ".npy" and os.path.splitext(label_file)[1] == ".npy":
        arr_img = np.load(os.path.join(path_img, img_file))
        arr_label = np.load(os.path.join(path_label, label_file)) 
        npy_to_nii(arr_img, f"../data/validation/experimental/img/sample_{i}_0000.nii.gz")
        npy_to_nii(arr_label, f"../data/validation/experimental/label/sample_{i}.nii.gz")
    elif os.path.splitext(img_file)[1] == ".nrrd" and os.path.splitext(label_file)[1] == ".nrrd":
        seg_nrrd_to_nii(os.path.join(path_img, img_file), f"../data/validation/experimental/img/sample_{i}_0000.nii.gz")
        seg_nrrd_to_nii(os.path.join(path_label, label_file), f"../data/validation/experimental/label/sample_{i}.nii.gz")
    elif os.path.splitext(label_file)[1] == ".nrrd":
        arr_img = np.load(os.path.join(path_img, img_file))
        npy_to_nii(arr_img, f"../data/validation/experimental/img/sample_{i}_0000.nii.gz")
        seg_nrrd_to_nii(os.path.join(path_label, label_file), f"../data/validation/experimental/label/sample_{i}.nii.gz")
    else:
        arr_label = np.load(os.path.join(path_label, label_file))
        seg_nrrd_to_nii(os.path.join(path_img, img_file), f"../data/validation/experimental/img/sample_{i}_0000.nii.gz")
        npy_to_nii(arr_label, f"../data/validation/experimental/label/sample_{i}.nii.gz")

# %%
