from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from filters import *
import numpy as np

IMAGE_WIDTH, IMAGE_HEIGHT = 400, 400
R, G, B = 0, 1, 2

class Application:
    def __init__(self, master):
        self.select_image_btn = Button(master, text="Open finder", command=self.open_finder).place(relx="0.5", anchor=N)
        #self.code_in_app_filter_btn = Button(master, text="CodeInPlace", command=code_in_place_filter).place(relx="0.3", rely="0.9", anchor=N)

        self.master = master
        self.selected_image = None
        self.resized_image = None
        self.final_image = None
        self.final_image_label = None

    def open_finder(self):
        self.master.filename = filedialog.askopenfilename(initialdir="/", title="Select your favorite picture", filetypes=(("png files", "*.png"),("jpg files", "*.jpg")))
        self.selected_image = Image.open(self.master.filename)
        self.resized_image = self.resize_with_aspect_ratio(self.selected_image)
        self.final_image = ImageTk.PhotoImage(self.resized_image)
        self.final_image_label = Label(image=self.final_image)
        self.final_image_label.image = self.final_image
        self.final_image_label.place(rely="0.1", relx="0.5", anchor=N)


    def resize_with_aspect_ratio(self, image):
        image_width = image.width
        image_height = image.height
        width_percent = IMAGE_WIDTH / float(image_width)
        new_height = int(float(image_height) * float(width_percent))
        return image.resize((IMAGE_WIDTH, new_height), Image.ANTIALIAS)


def main():
    root = Tk()
    root.title("Image Filter")
    root.geometry("750x750")

    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()