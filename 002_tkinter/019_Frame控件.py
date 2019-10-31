import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")

'''
框架控件
在屏幕上显示一个矩形区域，做容器使用
'''

frm = tkinter.Frame(win)
frm.pack()

frm1 = tkinter.Frame(frm)
tkinter.Label(frm1,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm1,text="左下",bg="blue").pack(side=tkinter.TOP)
frm1.pack(side=tkinter.LEFT)

frm2 = tkinter.Frame(frm)
tkinter.Label(frm2,text="右上",bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm2,text="右下",bg="yellow").pack(side=tkinter.TOP)
frm2.pack(side=tkinter.RIGHT)


win.mainloop()