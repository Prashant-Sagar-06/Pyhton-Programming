import os
import tkinter as tk
from PIL import Image, ImageTk

class ImageBrowser:
    def __init__(self, master, directory):
        self.master = master
        self.directory = directory
        self.image_files = os.listdir(directory)
        self.index = 0

        self.image_label = tk.Label(master, width=500, height=500)
        self.image_label.grid(row=0,column=0,columnspan=2)

        prev_button = tk.Button(master, text="Previous", command=self.prev_image)
        prev_button.grid(row=1,column=0)
        
        next_button = tk.Button(master, text="Next", command=self.next_image)
        next_button.grid(row=1, column=1)

        self.show_image()

    def show_image(self):
        image_file = os.path.join(self.directory, self.image_files[self.index])
        image = Image.open(image_file)
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo  

    def prev_image(self):
        self.index = (self.index - 1) % len(self.image_files)
        self.show_image()

    def next_image(self):
        self.index = (self.index + 1) % len(self.image_files)
        self.show_image()

root = tk.Tk()
app = ImageBrowser(root, "C:\\Users\\sagar\\OneDrive\\Desktop\\sagarimage")
root.mainloop()
