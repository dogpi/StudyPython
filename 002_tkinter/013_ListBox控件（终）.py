import tkinter

win = tkinter.Tk()
win.title("dogpi")




# MULTIPLE 支持多选
lb = tkinter.Listbox(win,selectmod=tkinter.MULTIPLE)
lb.pack()
for item in ["one","two","three","four","five","good","nice","cool","one","two","three","four","five","good","nice","cool"]:
    lb.insert(tkinter.END,item)


win.mainloop()