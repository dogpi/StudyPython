import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

label1 = tkinter.Label(win,text="good",bg="blue")
label2 = tkinter.Label(win,text="nice",bg="red")
label3 = tkinter.Label(win,text="cool",bg="pink")
label4 = tkinter.Label(win,text="haha",bg="yellow")

# 表格布局
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)

win.mainloop()