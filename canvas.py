# _*_ coding: utf-8 _*_
"""Canvas Weidgt

Canvas weidgt is the container of image and graph.
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
image_file = tk.PhotoImage(file='canvas_test.jpg')
# anchor参数是图片的锚点，意思是将图片锚点放置到前两个参数规定的点上，例如anchor='center',前两个位置参数为(0, 0)，则将图片的中心放置到(0, 0)
image = canvas.create_image(0, 0, anchor='nw', image=image_file)

canvas.pack()

def move_it():
    pass

move_button = tk.Button(window, text='move', command=lambda: move_it()).pack()

window.mainloop()