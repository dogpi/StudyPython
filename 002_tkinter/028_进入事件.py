import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")


label = tkinter.Label(win,text="dogpi is a good dog",bg="red")
label.pack()

def func(event):
    print(event.x,event.y)
# Enter:当鼠标进入控件时触发
label.bind("<Enter>",func)





win.mainloop()