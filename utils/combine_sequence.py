import os
import nibabel as nib
import numpy as np

# Define the directory containing the NIfTI files and the output file name
nii_directory = '/mnt/hdd1/karson/storage/SAMResults/sequence_syn_exp/sequence_syn_exp/pred/heart/hearts'
output_file = '/mnt/hdd1/karson/storage/SAMResults/syn_exp_combined_volumes.npy'

# List to hold the volumes
volumes = []

# Loop over all files in the directory
for filename in sorted(os.listdir(nii_directory), key=lambda x: int(x.split('_')[1])):
    if filename.endswith('img.nii.gz'):
        # print(filename)
        filepath = os.path.join(nii_directory, filename)
        nii = nib.load(filepath)
        data = nii.get_fdata()
        volumes.append(data)

# Stack all volumes into a single NumPy array
combined_volumes = np.stack(volumes, axis=0)
print(combined_volumes.shape)

# Save the combined volumes as a NumPy file
np.save(output_file, combined_volumes)

print(f"Combined volumes saved to {output_file}")
