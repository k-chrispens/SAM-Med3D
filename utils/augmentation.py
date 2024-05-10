"""Augmenting experimental data using rotations and scaling. Adapted from original code by Jan Christoph and Lucas.

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 5/9/2024
"""

#%%
import os
import numpy as np
from scipy.ndimage import rotate

foldername = 'data/experimental_hearts/'

def crop_pad_3d_volume(volume, target_shape=(128, 128, 128)):
    """
    Crop or pad a 3D volume to the target shape.

    Parameters:
        volume (numpy.ndarray): The input 3D volume.
        target_shape (tuple): The target shape of the volume after cropping or padding.

    Returns:
        numpy.ndarray: The cropped or padded 3D volume.
    """
    cropped_volume = np.zeros(target_shape)

    # Calculate the indices for cropping or padding
    start_idx = np.maximum((np.array(volume.shape) - np.array(target_shape)) // 2, 0)
    end_idx = start_idx + np.minimum(volume.shape, target_shape)

    # Calculate the slice indices for cropping
    crop_start = np.maximum((np.array(target_shape) - np.array(volume.shape)) // 2, 0)
    crop_end = crop_start + np.minimum(volume.shape, target_shape)

    # Crop or pad the volume
    cropped_volume[crop_start[0]:crop_end[0], crop_start[1]:crop_end[1], crop_start[2]:crop_end[2]] = volume[start_idx[0]:end_idx[0], start_idx[1]:end_idx[1], start_idx[2]:end_idx[2]]

    return cropped_volume

def augment_and_save(source_folder, destination_folder, num_rotations=24, scaling_factors=[ 0.9,0.95, 1.0,1.05, 1.1]):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # List all numpy files in the source folder
    numpy_files = [file for file in os.listdir(source_folder) if file.endswith('.npy')]

    for file in numpy_files:
        # Load the original numpy array
        file_path = os.path.join(source_folder, file)
        original_data = np.load(file_path)

        # Ensure the original data has the desired dimensions (128, 128, 128)
        if original_data.shape != (128, 128, 128):
            original_data = crop_pad_3d_volume(original_data, target_shape=(128, 128, 128))
            # raise ValueError(f"The dimensions of {file} are not (128, 128, 128).")

        # Perform rotations and scaling
        for rotation_idx, rotation_angle in enumerate(range(0, 360, 360 // num_rotations), start=1):
            for scaling_factor_idx, scaling_factor in enumerate(scaling_factors, start=1):
                rotated_data = rotate(original_data, rotation_angle, axes=(0, 1), reshape=False)

                # Ensure the rotated data has the desired dimensions
                cropped_data = rotated_data[:128, :128, :128]

                # Save the augmented image
                save_path = os.path.join(destination_folder, f"{file.replace('.npy', f'_rot_{rotation_angle}_scale_{scaling_factor:.2f}.npy')}")
                np.save(save_path, cropped_data)

# Usage example
                
source_folder = foldername + 'segmentations/'
destination_folder = foldername + 'segmentations/augmented/'

augment_and_save(source_folder, destination_folder)
# %%

import os
import glob
import numpy as np
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.colors import colorConverter

foldername = 'data/experimental_hearts/'
foldername_us = foldername + 'ultrasound/augmented/'
foldername_sg = foldername + 'segmentations/augmented/'

print('loading data from ' + str(foldername_us))

list_us_npy_files = sorted(glob.glob(foldername_us + '*.npy'))
list_sg_npy_files = sorted(glob.glob(foldername_sg + '*.npy'))

n_files = len(list_us_npy_files)
print('number of segmentations: ' + str(n_files))
for i in range(n_files):
    print(list_us_npy_files[i] + str('\t\t\t') + list_sg_npy_files[i])



#%%

i = random.randint(0,n_files-1)
print('pick a random file: ' + str(i))



us_filename = list_us_npy_files[i]
sg_filename = list_sg_npy_files[i]

us = np.load(us_filename)
sg = np.load(sg_filename)

print('selecting: ' + us_filename)
print('selecting: ' + sg_filename)


d = us.shape[0]
dw = 10 # how much random offset you want from the center plane
c1 = int(d/2) + random.randint(-dw,dw) # pick a random cross-section at center pm 5
c2 = int(d/2) + random.randint(-dw,dw)
c3 = int(d/2) + random.randint(-dw,dw)



color1 = colorConverter.to_rgba('black',alpha=0.0)
color2 = colorConverter.to_rgba('red')

# make the colormap
cmap_mask = mpl.colors.LinearSegmentedColormap.from_list('my_cmap2',[color1,color2],256)

cmap_mask._init() # create the _lut array, with rgba values

# create your alpha array and fill the colormap with them.
# here it is progressive, but you can create whathever you want
alphas = np.linspace(0, 0.25, cmap_mask.N+3)
cmap_mask._lut[:,-1] = alphas

#img2 = plt.imshow(zvals, interpolation='nearest', cmap=cmap1, origin='lower')
#img3 = plt.imshow(zvals2, interpolation='nearest', cmap=cmap2, origin='lower')

print('displaying manual 3D segmentations ... segmentation ' + str(i))

fig, ax = plt.subplots(3, 3)
ax[0,0].imshow(np.squeeze(us[c1,:,:]), cmap='gray')
ax[0,1].imshow(np.squeeze(us[:,c2,:]), cmap='gray')
ax[0,2].imshow(np.squeeze(us[:,:,c3]), cmap='gray')
ax[1,0].imshow(np.squeeze(sg[c1,:,:]), cmap='gray')
ax[1,1].imshow(np.squeeze(sg[:,c2,:]), cmap='gray')
ax[1,2].imshow(np.squeeze(sg[:,:,c3]), cmap='gray')
ax[2,0].imshow(np.squeeze(us[c1,:,:]), cmap='gray')
ax[2,0].imshow(np.squeeze(sg[c1,:,:]), cmap=cmap_mask)
ax[2,1].imshow(np.squeeze(us[:,c2,:]), cmap='gray')
ax[2,1].imshow(np.squeeze(sg[:,c2,:]), cmap=cmap_mask)
ax[2,2].imshow(np.squeeze(us[:,:,c3]), cmap='gray')
ax[2,2].imshow(np.squeeze(sg[:,:,c3]), cmap=cmap_mask)



# %%
