import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
tk.Label(window, text='on the window').pack()

frm = tk.Frame(window)
frm.pack()
frm_left = tk.Frame(frm)
frm_right = tk.Frame(frm)
# pack中的side参数表示pack时的位置
frm_left.pack(side='left')
frm_right.pack(side='right')

tk.Label(frm_left, text='on the frm_left1').pack()
tk.Label(frm_left, text='on the frm_left2').pack()
tk.Label(frm_right, text='on the frm_right1').pack()
window.mainloop()
