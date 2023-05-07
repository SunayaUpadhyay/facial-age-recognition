# Face Age Group Classification- By Sunaya Upadhyay and Aditya Gupta

This project is aimed at developing a machine learning model that can classify faces into three age groups: old, young, and middle. The model will use image processing techniques and machine learning algorithms to accurately categorize faces into the appropriate age group.

## Data Collection

The images for our project have been taken from the IMDB-WIKI dataset. However, various modifications have been made to the dataset in order to make it usable for our project. This includes selecting a smaller subset of images, dividing them into various classes (i.e., OLD, MIDDLE and YOUNG), selecting images with just faces in them, cropping the faces from the images using the haar cascade algorithm and finally making a csv file of all image ids and their respective classes. You can find the dataset at this link: https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/. We used the following python scripts:

- filter.py: pastes the images into different folders based on their class (i.e., OLD, MIDDLE and YOUNG)
- combine+excel.py: combines the images from the three folders into one folder in a random order and also makes a csv file containing image ids and their respective classes.
- crop.py: copies all the cropped faces from the images into another directory.
- diff.py: returns the ids of images that the algorithm wasn't able to crop so that they can be deleted from the csv file.

## Installation

1. Clone this repository to your local machine using the following command: https://github.com/SunayaUpadhyay/facial-age-recognition

2. Install the required dependencies using the following commands:

- numpy &nbsp;&nbsp; `pip install numpy`
- pandas &nbsp;&nbsp; `pip install pandas`
- matplotlib&nbsp;&nbsp; `pip install matplotlib`
- os&nbsp;&nbsp; `pip install os`
- skimage&nbsp;&nbsp; `pip install skimage`
- tqdm&nbsp;&nbsp; `pip install tqdm`
- cv2&nbsp;&nbsp; `pip install cv2`
- scikit-learn&nbsp;&nbsp; `pip install scikit-learn`
- keras&nbsp;&nbsp; `pip install keras`
- time &nbsp;&nbsp; `pip install time`

## Usage
To test the model on a new image, run the attached python file window.py and click on "Open Image" to be able to select an image that you wish to get the prediction for. Then, click on "Get Prediction" to view the prediction.
## License
Copyright 2023 Sunaya Upadhyay and Aditya Gupta

Licensed under the Apache License, Version 2.0 ("License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.




