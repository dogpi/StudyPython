import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")


label = tkinter.Label(win,text="dogpi is a good dog",bg="red")
# 设置焦点
label.focus_set()
label.pack()

def func(event):
    print("Shift")


# Shift_L:左Shift按键
# Shift_R:右Shift按键
# F5:
# Return:回车键
# BackSpace:退格键
label.bind("<Shift_L>",func)

win.mainloop()
