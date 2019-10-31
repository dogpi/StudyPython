import tkinter

def func():
    print("dogpi is a good dog")

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

button = tkinter.Button(win,text="button",command=func)
button.pack()
button2 = tkinter.Button(win,text="button2",command=lambda :print("dogpi is a good man"))
button2.pack()


win.mainloop()