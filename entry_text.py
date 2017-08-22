import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# show表示entry是否显示输入的字符，如果show='*'，则显示为*****的密码格式；如果show=None，则显示输入的字符；show中传入什么字符，就会打印成该字符
entry = tk.Entry(window, show='*')
entry.pack()

# tk.Entry实例的get方法可以获得Entry中输入的文字
# tk.Text实例的insert方法可以插入文字，其中第一个参数是插入位置，'insert'表示插入至光标所在处，'end'表示i插入尾部
def insert_point(entry, text):
    var = entry.get()
    text.insert('insert', var)

def insert_end(entry, text):
    var = entry.get()
    text.insert('end', var)

# 可以使用lambda函数给command传入参数
button_insert_point = tk.Button(
    window, text='insert point', width=15, height=2, command=lambda: insert_point(entry, text))
button_insert_point.pack()

button_insert_end = tk.Button(
    window, text='insert end', command=lambda: insert_end(entry, text))
button_insert_end.pack()

text = tk.Text(window, height=2)
text.pack()

window.mainloop()
