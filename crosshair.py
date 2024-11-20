import tkinter as tk
from PIL import Image, ImageTk

IMAGE_PATH = "images.png"  

root = tk.Tk()
root.title("Overlay Image")

root.overrideredirect(True)
root.attributes("-topmost", True)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

image = Image.open(IMAGE_PATH).convert("RGBA")  
image = image.resize((50, 50), Image.Resampling.LANCZOS)  

image_tk = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0, bg="white")
canvas.pack(fill="both", expand=True)

center_x = screen_width // 2
center_y = screen_height // 2

canvas.create_image(center_x, center_y, image=image_tk, anchor="center")

root.attributes("-transparentcolor", "white")

root.geometry(f"{screen_width}x{screen_height}+0+0")

root.mainloop()
