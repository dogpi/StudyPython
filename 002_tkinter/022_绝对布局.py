import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

label1 = tkinter.Label(win,text="good",bg="blue")
label2 = tkinter.Label(win,text="nice",bg="red")
label3 = tkinter.Label(win,text="cool",bg="pink")

# 绝对布局
label1.place(x=10,y=10)
label2.place(x=50,y=50)
label3.place(x=100,y=100)

win.mainloop()