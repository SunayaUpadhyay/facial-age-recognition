import os
import random
import shutil

# Define the destination folder for the combined images
combined_folder = '/Users/adityagupta/Desktop/Train temp'

# Define the source folders for the different age groups
old_folder = '/Users/adityagupta/Desktop/old'
middle_folder = '/Users/adityagupta/Desktop/middle'
young_folder = '/Users/adityagupta/Desktop/young'
age_classes = {
old_folder: 'OLD',
middle_folder: 'MIDDLE',
young_folder: 'YOUNG'
}

# Combine the images from the source folders into a list
image_list = []
for folder in [old_folder, middle_folder, young_folder]:
    for image_file in os.listdir(folder):
        if image_file.endswith('.jpg'):
            image_list.append((os.path.join(folder, image_file), folder))

# Shuffle the image list randomly
random.shuffle(image_list)

# Copy the images to the combined folder and rename them starting from 1
for i, (image_path, folder) in enumerate(image_list):
    image_name = f"{i+1:04}.jpg"
    csv_name = f"{i+1:04}"
    destination_path = os.path.join(combined_folder, image_name)
    shutil.copy(image_path, destination_path)
    # Write the image id and corresponding claTrTrass to a CSV file
    class_name = age_classes[folder]
    with open(os.path.join(combined_folder, 'train.csv'), 'a') as f:
        f.write(f"{csv_name},{class_name}\n")

