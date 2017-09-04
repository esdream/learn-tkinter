import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title('Welcome to my Python Software!')
window.geometry('450x300')

canvas = tk.Canvas(window, height=200, width=500)
image_file = Image.open('welcome.jpg')
canvas.image = ImageTk.PhotoImage(image_file)
image = canvas.create_image(0, 300, image=canvas.image)
canvas.pack(side='top')

window.mainloop()
