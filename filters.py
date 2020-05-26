from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from filters import *
import numpy as np
import os

IMAGE_WIDTH, IMAGE_HEIGHT = 400, 400
R, G, B = 0, 1, 2

class Application:
    def __init__(self, master):
        self.master = master
        self.selected_image = None
        self.resized_image = None
        self.final_image = None
        self.final_image_label = None
        self.filtered_image = None
        self.filtered_photo = None
        self.saved_image_counter = 0

        self.select_image_btn = Button(master, text="Open finder", command=self.open_finder).place(relx="0.5", anchor=N)
        self.code_in_place_filter_btn = Button(master, text="CodeInPlace", command=self.code_in_place_filter).place(relx="0.3", rely="0.9", anchor=N)
        self.save_filtered_image_btn = Button(master, text="Save", command=self.save_to_repo).place(relx="0.6", anchor=N)        

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

    def code_in_place_filter(self):
        copied_image = self.resized_image.copy()
        pixels = np.array(copied_image).astype(np.float)
        for x in range(copied_image.height):
            for y in range(copied_image.width):
                pixels[x, y, R] = self.clamp(pixels[x, y, R] * 1.5)
                pixels[x, y, G] = self.clamp(pixels[x, y, G] * 0.7)
                pixels[x, y, B] = self.clamp(pixels[x, y, B] * 1.5)

        self.filtered_image = Image.fromarray(pixels.astype(np.uint8))
        self.filtered_photo = ImageTk.PhotoImage(self.filtered_image)
        self.final_image_label.configure(image=self.filtered_photo)
        self.final_image_label.image = self.filtered_photo

    def save_to_repo(self):
        image_name = "image_" + str(self.saved_image_counter) + ".jpg"
        file_path = os.path.join('filtered_image/', image_name)
        self.filtered_image.save(file_path, "JPEG")
        self.saved_image_counter += 1


    def clamp(self, num):
        num = int(num)
        if num < 0:
            return 0
        if num >= 256:
            return 255
        return num


def main():
    root = Tk()
    root.title("Image Filter")
    root.geometry("750x750")

    app = Application(root)
    root.mainloop()


if __name__ == '__main__':
    main()