import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to open an image file
def open_image():
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    image = image.convert("RGB")
    image.thumbnail((400, 400))  # Resize image to fit in the window
    update_canvas(image)


# Function to update canvas with processed image
def update_canvas(image):
    canvas.delete("all")  # Clear previous image from canvas
    processed_image = process_image(image)
    processed_image_tk = ImageTk.PhotoImage(processed_image)
    canvas.image_tk = processed_image_tk  # Keep a reference to the image to prevent garbage collection
    canvas.create_image(
        canvas_width / 2, canvas_height / 2, anchor=tk.CENTER, image=processed_image_tk
    )


# Dummy function for image processing with ML model
def process_image(image):
    # Placeholder for ML model processing logic
    # In this example, simply flip the image horizontally
    processed_image = image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
    return processed_image


# Function to get prediction
def get_prediction():
    # Placeholder for ML model prediction logic
    prediction = "Dummy Prediction"  # Replace with actual prediction logic
    prediction_label.config(text="Prediction: " + prediction)


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
