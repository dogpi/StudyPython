import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

def func(event):
    print(event.x,event.y,event.x_root,event.y_root)

button1 = tkinter.Button(win,text="leftmouse button")
button1.bind("<Button-1>",func)
button1.pack()

label1 = tkinter.Label(win,text="leftmouse label")
label1.bind("<Button-1>",func)
label1.pack()
'''
<Button-1>:鼠标左键
<Button-2>:鼠标中键
<Button-3>:鼠标右键
<Double-Button-1>:左键双击
<Double-Button-2>:中键双击
<Double-Button-3>:右键双击
<Triple-Button-1>:左键三击
<Triple-Button-2>:中键三击
<Triple-Button-3>:右键三击
'''









win.mainloop()