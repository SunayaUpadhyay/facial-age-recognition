import os
import datetime
import cv2

# Define the source folder containing the images
source_folder = '/Users/adityagupta/Desktop/t'

# Define the destination folders for the different age groups
old_folder = '/Users/adityagupta/Desktop/old'
middle_folder = '/Users/adityagupta/Desktop/middle'
young_folder = '/Users/adityagupta/Desktop/young'

# Load the pre-trained face detection classifier from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Get a list of all the image files in the source folder
image_files = [f for f in os.listdir(source_folder) if f.endswith('.jpg')]
old_count = len(os.listdir(old_folder))
young_count = len(os.listdir(young_folder))
middle_count = len(os.listdir(middle_folder))
# Loop through each image file and process it
for image_file in image_files:
    # Extract the birth year and year of photo from the filename

    birth_year_str = image_file.split('_')[1][:4]
    birth_year = None
    if len(birth_year_str) == 4 and birth_year_str.isdigit():
        birth_year = int(birth_year_str)

    photo_year_str = image_file.split('_')[2][:4]
    photo_year = None
    if len(photo_year_str) == 4 and photo_year_str.isdigit():
        photo_year = int(photo_year_str)

    # Calculate the person's age
    if birth_year != None and photo_year != None:
        age = photo_year - birth_year
        print(age)
    # Load the image and detect faces
    image_path = os.path.join(source_folder, image_file)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Move the image file to the appropriate destination folder based on age and face detection
    if age >= 60 and len(faces) > 0:
        if old_count < 2200:
            destination_folder = old_folder
            destination_path = os.path.join(destination_folder, image_file)
            if not os.path.exists(destination_path):
                os.rename(image_path, destination_path)
                old_count+=1
        elif age >= 30 and age < 60 and len(faces) > 0:
            if middle_count < 2200:
                destination_folder = middle_folder
                destination_path = os.path.join(destination_folder, image_file)
                if not os.path.exists(destination_path):
                    os.rename(image_path, destination_path)
                    old_count += 1
        elif age > 0 and age < 30:
            if young_count < 6000:
                destination_folder = old_folder
                destination_path = os.path.join(destination_folder, image_file)
                if not os.path.exists(destination_path):
                    os.rename(image_path, destination_path)
                    old_count += 1
            else:
                break
