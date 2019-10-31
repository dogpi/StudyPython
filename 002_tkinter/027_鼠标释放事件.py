import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")


label = tkinter.Label(win,text="dogpi is a good dog",bg="red")
label.pack()

def func(event):
    print(event.x,event.y)

label.bind("<ButtonRelease-1>",func)
'''
<ButtonRelease-1>:鼠标左键释放
<ButtonRelease-2>:鼠标中键释放
<ButtonRelease-3>:鼠标右键释放
'''




win.mainloop()