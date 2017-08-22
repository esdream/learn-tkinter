import tkinter as tk

window = tk.Tk()
window.title('my window')
# 这里的window.geometry是窗口大小，传入的字符串参数中的x是英文字母x
window.geometry('400x300')

# 作为窗口使用的变量，需要设置成tkinter中的变量形式
var_string = tk.StringVar()
# 将text设置为变量，传入textvariable参数
label = tk.Label(window, textvariable=var_string, bg='blue',
                 font=('Arial', 12), width=15, height=2)

# pack是一种自动布局的方法
label.pack()
on_hit = False
def hit_me():
    global on_hit
    if(on_hit == False):
        on_hit = True
        # Stringvar变量通过set设置
        var_string.set('You hit me')
    else:
        on_hit = False
        var_string.set('Wait for next hit')

# 点击按钮后执行的命令用command传入
button = tk.Button(window, text='hit me', width=15, height=2, command=hit_me)
button.pack()

# 创建队列循环
window.mainloop()
