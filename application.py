from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from filters import *
import numpy as np

IMAGE_WIDTH, IMAGE_HEIGHT = 400, 400
R, G, B = 0, 1, 2
root = Tk()
root.title("Image Filter")
root.geometry("750x750")
my_image = None
final_image = None
final_image_label = None

def open_finder():
    global my_image
    global final_image_label
    global final_image
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select your favorite picture", filetypes=(("png files", "*.png"),("jpg files", "*.jpg")))
    my_image = Image.open(root.filename)
    # Resize Image Calculation
    width_percent = IMAGE_WIDTH / float(my_image.width)
    new_height = int(float(my_image.height) * float(width_percent))
    # Update original image with its resized version, and display in Label
    my_image = my_image.resize((IMAGE_WIDTH, new_height), Image.ANTIALIAS)
    final_image = ImageTk.PhotoImage(my_image)
    final_image_label = Label(image=final_image)
    final_image_label.image = final_image
    final_image_label.place(rely="0.1", relx="0.5", anchor=N)

def clamp(num):
    num = int(num)
    if num < 0:
        return 0
    if num >= 256:
        return 255
    return num

def code_in_place_filter():
     global final_image_label
     global final_image
     copied_image = my_image.copy()
     pixels = np.array(copied_image).astype(np.float)
     for x in range(copied_image.height):
        for y in range(copied_image.width):
            pixels[x, y, R] = clamp(pixels[x, y, R] * 1.5)
            pixels[x, y, G] = clamp(pixels[x, y, G] * 0.7)
            pixels[x, y, B] = clamp(pixels[x, y, B] * 1.5)

     filtered_image = Image.fromarray(pixels.astype(np.uint8))
     ph = ImageTk.PhotoImage(filtered_image)
     final_image_label.configure(image=ph)
     final_image_label.image = ph


my_btn = Button(root, text="Open finder", command=open_finder).place(relx="0.5", anchor=N)
filter_btn = Button(root, text="CodeInPlace", command=code_in_place_filter).place(relx="0.3", rely="0.9", anchor=N)
root.mainloop()