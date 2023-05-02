import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2
from keras.models import load_model


# Load saved Keras model
model = load_model("D:\College\ML\Project\CNN.h5")

# Function to open an image file
def open_image():
    global image_path, image_tk
    image_path = filedialog.askopenfilename()
    image = Image.open(image_path)
    image = image.convert("RGB")
    image.thumbnail((400, 400))  # Resize image to fit in the window
    image_tk = ImageTk.PhotoImage(image)
    canvas.create_image(canvas_width / 2, canvas_height / 2, image=image_tk)


# Image preprocessing
def preprocess_image(img):
    if img.shape[-1] == 4:
        img = img[..., :3]  # remove alpha channel
    img = cv2.convertScaleAbs(img)
    img = cv2.resize(img, (128, 128))
    img = np.expand_dims(img, axis=0)
    # Normalize pixel values
    return img


def get_prediction():
    # Get processed image
    image = Image.open(image_path)
    print(np.array(image))
    img = np.array(image)
    processed_image = preprocess_image(np.array(image))
    # Use model to make prediction
    prediction = model.predict(processed_image)

    # Convert prediction to class label
    class_label = np.argmax(prediction, axis=1)[0]
    print(prediction)

    # Update prediction label
    if class_label == 0:
        prediction_label.config(text="Prediction: Young ")
    elif class_label == 1:
        prediction_label.config(text="Prediction: Middle")
    else:
        prediction_label.config(text="Prediction: Old")


# Create main window
root = tk.Tk()
root.title("Image Processor")

# Set window size and position
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set window background color
root.configure(bg="#E8E8E8")

# Create canvas to display image
canvas_width = 400  # Canvas width
canvas_height = 400  # Canvas height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#FFFFFF")
canvas.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

# Create open button
open_button = tk.Button(
    root,
    text="Open Image",
    command=open_image,
    bg="#4CAF50",
    fg="#FFFFFF",
    relief=tk.RAISED,
    font=("Helvetica", 14),
)
open_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Create get prediction button
get_prediction_button = tk.Button(
    root,
    text="Get Prediction",
    command=get_prediction,
    bg="#FFC107",
    fg="#FFFFFF",
    relief=tk.RAISED,
    font=("Helvetica", 14),
)
get_prediction_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Create prediction label
prediction_label = tk.Label(root, text="", bg="#E8E8E8", font=("Helvetica", 16))
prediction_label.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Start Tkinter event loop
root.mainloop()
