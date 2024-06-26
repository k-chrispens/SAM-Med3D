#!/bin/bash

dir="data/synthetic_50/heart/hearts/labelsTr/"

cd "$dir"

for file in segmentation_*.nii.gz
do
    num=${file#segmentation_}
    num=${num%.nii.gz}

    new_name="sample_$num.nii.gz"

    mv "$file" "$new_name"
done