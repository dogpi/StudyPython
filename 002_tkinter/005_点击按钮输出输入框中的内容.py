import tkinter

def getStr():
    print(entry.get())

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")


# 绑定变量
entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text="button",command=getStr)
button.pack()
win.mainloop()