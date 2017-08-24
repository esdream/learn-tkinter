# _*_ coding: utf-8 _*_
"""Menubar

Menubar widget is at the top of window.
"""

import tkinter as tk

window = tk.Tk()
window.title('Menu Bar')
window.geometry('400x300')

label = tk.Label(window, text='', bg='yellow')
label.pack()

global count
count = 0
def do_job():
    global count
    label.config(text='do'+str(count))
    count += 1

# tk.Menu()中的参数表示的是当前Menubar的上一层widget，例如这里menubar变量的上一层是window，表示menubar依附在window上
menubar = tk.Menu(window)
# tearoff参数表示menubar widget能够从window中独立出来，0表示不能，1表示能
filemenu = tk.Menu(menubar, tearoff=1)
# add_cascade表示在menubar中增加一个瀑布栏(cascade)，下方的command命令可以放置在瀑布栏中
menubar.add_cascade(label='file', menu=filemenu)
filemenu.add_command(label='New', command=lambda: do_job())
filemenu.add_command(label='Open', command=lambda: do_job())
filemenu.add_command(label='Save', command=lambda: do_job())
# filemenu.add_separator()会创建一条分割线
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=lambda: do_job())
editmenu.add_command(label='Copy', command=lambda: do_job())
editmenu.add_command(label='Paste', command=lambda: do_job())
# 创建子menubar
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu1', command=do_job)
# 整个menubar创建好后，必须用window.config(menu=menubar)集成至window中
window.config(menu=menubar)

window.mainloop()
