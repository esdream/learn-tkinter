import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

# 改变组件中文字的另一种方法，使用tk.Label实例的config方法。这种方法可以修改组件的任何属性
def print_selection(label, var):
    label.config(text='you have selected ' + var.get())

# tk.Radiobutton()中，variable和value参数表示，当该单选按钮被选中时，令variable的值等于value
radio_button1 = tk.Radiobutton(
    window, text='Option A', variable=var, value='A', command=lambda: print_selection(label, var))
radio_button1.pack()

radio_button2 = tk.Radiobutton(
    window, text='Option B', variable=var, value='B', command=lambda: print_selection(label, var))
radio_button2.pack()

radio_button3 = tk.Radiobutton(
    window, text='Option C', variable=var, value='C', command=lambda: print_selection(label, var))
radio_button3.pack()

window.mainloop()
