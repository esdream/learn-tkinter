import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

label = tk.Label(window, bg='yellow', width=20, text='empty')
label.pack()


def print_selection(label):
    if(var1.get() == 1) & (var2.get() == 0):
        label.config(text='I love only Python')
    elif(var1.get() == 0) & (var2.get() == 1):
        label.config(text='I love only C++')
    elif(var1.get() == 0) & (var2.get() == 0):
        label.config(text='I do not love either')
    else:
        label.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()

# onvalue参数表示被选中时，variable的值；offvalue表示未被选中时，variable的值
c1 = tk.Checkbutton(window, text='Python', variable=var1,
                    onvalue=1, offvalue=0, command=lambda: print_selection(label))
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1,
                    offvalue=0, command=lambda: print_selection(label))
c2.pack()

window.mainloop()
