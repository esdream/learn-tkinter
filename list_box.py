import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var1 = tk.StringVar()
label = tk.Label(window, bg='yellow', width=4, textvariable=var1)
label.pack()

# 要提取ListBox中的内容，使用list_box.get()获得（和entry.get()一样），获得的list item由list_box.curselection()指定为指针指向的位置.当然也可以直接传入索引位置
def print_selection(list_box):
    value = list_box.get(list_box.curselection())
    var1.set(value)

button_print_selection = tk.Button(
    window, text='print selection', width=15, height=2, command=lambda: print_selection(list_box))
button_print_selection.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))
list_box = tk.Listbox(window, listvariable=var2)
list_items = [1, 2, 3, 4]
for item in list_items:
    # 插入到list_box的尾部，类似于append
    list_box.insert('end', item)

list_box.insert(1, 'first')
list_box.insert(2, 'second')
list_box.delete(2)
list_box.pack()

window.mainloop()
