import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")



def func(event):
    print("event")



win.bind("<Control-Alt-b>",func)
win.bind("<Control-a>",func)
win.bind("<Shift-Up>",func)






win.mainloop()