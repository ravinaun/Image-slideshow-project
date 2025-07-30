'''This is the best solution'''

#list of image path
import tkinter as tk
from PIL import Image, ImageTk
import itertools
import os

# List of image file paths
image_folder = "images"  # Change this to your image folder
image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder)
               if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))]

# Create image objects
images = [Image.open(img).resize((500, 350)) for img in image_files]
image_cycle = itertools.cycle(images)  # Create an endless iterator

# Initialize main window
root = tk.Tk()
root.title("Image Slideshow")
root.geometry("520x380")
root.configure(bg="black")

# Label to display images
image_label = tk.Label(root, bg="black")
image_label.pack(padx=10, pady=10)

# Function to update image
def update_image():
    img = next(image_cycle)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo  # Keep a reference!
    root.after(3000, update_image)  # Change every 3 seconds

# Start the slideshow
update_image()
root.mainloop()
