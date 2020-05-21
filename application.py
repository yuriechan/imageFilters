from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from filters import *

IMAGE_WIDTH, IMAGE_HEIGHT = 400, 400

root = Tk()
root.title("Image Filter")

def open_finder():
    global my_image
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
    final_image_label.pack()


my_btn = Button(root, text="Open finder", command=open_finder).pack()

root.mainloop()
