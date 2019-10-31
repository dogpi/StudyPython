import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")


label = tkinter.Label(win,text="dogpi is a good dog")
label.pack()

def func(event):
    print(event.x,event.y)

label.bind("<B1-Motion>",func)
'''
<B1-Motion>:按下鼠标左键移动
<B2-Motion>:按下鼠标中键移动
<B3-Motion>:按下鼠标右键移动
'''




win.mainloop()