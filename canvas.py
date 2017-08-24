# _*_ coding: utf-8 _*_
"""Canvas Widget

Canvas widget is the container of image and graph.
"""

import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title('my window')
window.geometry('800x400')

canvas = tk.Canvas(window, bg='blue', height=600, width=400)
# PhotoImage只支持gif或BMP格式图片
image_file = tk.PhotoImage(file='canvas_test.gif')
# anchor参数是图片的锚点，意思是将图片锚点放置到前两个参数规定的点上，例如anchor='center',前两个位置参数为(0, 0)，则将图片的中心放置到(0, 0)
tkimage = canvas.create_image(0, 0, anchor='nw', image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
# 绘制线条
line = canvas.create_line(x0, y0, x1, y1)
# 绘制圆形
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')
# 绘制弧形，start是启示弧度，extent是终止弧度，按逆时针绘制
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=90, extent=210)
# 绘制长方形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)

# 使用ImageTk在canvas插入jpg格式图片
image_jpg = Image.open('canvas_test.jpg')
canvas.image = ImageTk.PhotoImage(image_jpg)
canvas.create_image(0, 300, image=canvas.image, anchor='nw')

canvas.pack()

def move_it(canvas, move_object):
    canvas.move(rect, 1, 2)

move_button = tk.Button(window, text='move',
                        command=lambda: move_it(canvas, rect)).pack()



window.mainloop()
