import cv2
import os

# specify the path to the input directory containing the images
input_dir = '/Users/adityagupta/Desktop/Train temp'
output_dir = '/Users/adityagupta/Desktop/Train'

# load the pre-trained Haar cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
c=0
# loop through all the image files in the input directory that have a .jpg extension
for filename in os.listdir(input_dir):
    if not filename.lower().endswith('.jpg'):
        continue

    # read the image file
    img = cv2.imread(os.path.join(input_dir, filename))
    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        # extract the face from the image
        face = img[y:y+h, x:x+w]
        # create a new filename for the extracted face by appending '_face' to the original filename
        face_filename = os.path.splitext(filename)[0] + '.jpg'
        # save the extracted face to the output directory
        cv2.imwrite(os.path.join(output_dir, face_filename), face)
        c+=1
print(c)
