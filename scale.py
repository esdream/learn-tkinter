import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()

def print_scale(var):
    label.config(text='you have selected' + var)

# scale是一个拖动条形式的控件。以下参数中，label是该控件显示的名字，from_ 至 to，orient是拖动条的方向，length是整个拖动条的长度，showvalue是拖动条处的值是否显示，设置为0不显示，设置为1显示。tickinterval表示拖动条标注的间隔，这里设置为3表示每隔3标注一次；resolution是拖动条显示数值的精度。
scale = tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL, length=200,
                 showvalue=0, tickinterval=3, resolution=0.01, command=print_scale)
scale.pack()

window.mainloop()
