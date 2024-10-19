import tkinter as tk
from tkinter import filedialog
from tkinter import Button, Label
from PIL import Image, ImageTk, ImageOps
import numpy as np
import tensorflow as tf

# Load the trained model
model_path = r"N:\UniVERSITY\TRI 2\ST1\Capstone\dataset\converted_keras\keras_model.h5"
model = tf.keras.models.load_model(model_path)

# Load the labels
labels_path = r"N:\UniVERSITY\TRI 2\ST1\Capstone\dataset\converted_keras\labels.txt"
with open(labels_path) as file:
    class_names = file.readlines()

def classify(test_image_path):
    disp_string = ''
    image = Image.open(test_image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    disp_string += "\n" + str(class_name[2:])
    disp_string += "\nConfidence Score:" + str(confidence_score)
    label.configure(foreground='#011638', text=disp_string)

def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image", command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        output_image.configure(image=im)
        output_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except Exception as e:
        print(f"Error: {e}")

# Initialize GUI
top = tk.Tk()
top.geometry('800x600')
top.title('Image Classifier')
top.configure(background='#CDCDCD')

label = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
output_image = Label(top)

upload = Button(top, text="Upload an Image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
upload.pack(side=tk.BOTTOM, pady=50)

output_image.pack(side=tk.BOTTOM, expand=True)
label.pack(side=tk.BOTTOM, expand=True)

heading = Label(top, text="Image Classification", pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()

top.mainloop()
