import tkinter as tk
# messagebox不会在导入messagebox时自动导入，需要使用以下导入方式
from tkinter import messagebox
# 或者import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

def hit_me():
    messagebox.showinfo(title='info', message='My friend')
    messagebox.showwarning(title='warning', message='My friend')
    messagebox.showerror(title='error', message='My friend')
    # messagebox.askquestion会返回yes or no
    print(messagebox.askquestion(title='ask question', message='yes or no'))

    # messagebox.askyesno会返回True or False
    print(messagebox.askyesno(title='ask yesno', message='yes or no'))

    # messagebox.askokcancel会返回True or False
    print(messagebox.askokcancel(title='ask okcancel', message='ok or cancel'))

tk.Button(window, text='hit me', command=hit_me).pack()
window.mainloop()
