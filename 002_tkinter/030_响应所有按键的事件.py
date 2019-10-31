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
    print("event.char =",event.char)
    print("event.keycode =",event.keycode)

# Key:响应所有按键
label.bind("<Key>",func)





win.mainloop()