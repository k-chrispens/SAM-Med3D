"""Add "training" to dataset.json

Author: Karson Chrispens (karson.chrispens@ucsf.edu)
Date: 4/26/2024
"""

import json

# Load the dataset.json file
path = "./data/experimental_hearts/dataset.json"

with open(path, "r+") as f:
    data = json.load(f)
    training_dict = {}
    for i in range(data["numTraining"]):
        training_dict[f"sample_{i}"] = {"label": f"sample_{i}.nii.gz", "image": f"sample_{i}.nii.gz"}
    data["training"] = training_dict

    # Save the updated dataset.json file
    json.dump(data, f)