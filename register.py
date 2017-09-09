import tkinter as tk
from tkinter import messagebox
import pickle
from PIL import ImageTk, Image

window = tk.Tk()
window.title('Welcome to my Python Software!')
window.geometry('800x600')

# welcome image
canvas = tk.Canvas(window, height=300, width=500)
image_file = Image.open('welcome.jpg')
# 制作缩略图
img_width, img_height = image_file.size
new_width = 500
new_height = float(new_width) / img_width * img_height
# image.thumbnail会将原图像对象变为缩略图
image_file.thumbnail((new_width, new_height), Image.ANTIALIAS)

canvas.image = ImageTk.PhotoImage(image_file)
image = canvas.create_image(0, 0, anchor='nw', image=canvas.image)
canvas.pack(side='top')

# user information
tk.Label(window, text='User name:').place(x=50, y=150)
tk.Label(window, text='Password:').place(x=50, y=190)

var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160, y=150)

var_usr_pwd = tk.StringVar()
entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_usr_pwd.place(x=160, y=190)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

    if(usr_name in usrs_info):
        if(usr_pwd == usrs_info[usr_name]):
            tk.messagebox.showinfo(title='Welcome', message='Hello, '+usr_name)
        else:
            tk.messagebox.showerror(message='Your password is error!')
    else:
        is_sign_up = tk.messagebox.askyesno(message='Welcome, You have not sign up yet. Need sign up?')
        if(is_sign_up):
            usr_sign_up()

def usr_sign_up():
    pass
# login and sign up button
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170, y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

window.mainloop()
