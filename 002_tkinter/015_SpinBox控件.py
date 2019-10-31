import tkinter

win = tkinter.Tk()
win.title("dogpi")

sp = tkinter.Spinbox(win,from_=0,to=100)
sp.pack()

# increment:步长，默认为1
sp1 = tkinter.Spinbox(win,from_=0,to=100,increment=5)
sp1.pack()

sp2 = tkinter.Spinbox(win,values=(0,2,4,6,8))
sp2.pack()

# 绑定变量
v = tkinter.IntVar()
sp3 = tkinter.Spinbox(win,from_=0,to=100,textvariable=v,command = lambda :print(v.get()))
sp3.pack()
# 设置值
v.set(20)
# 取值
print(v.get())



win.mainloop()
