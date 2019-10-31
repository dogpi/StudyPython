import tkinter

win = tkinter.Tk()
win.title("dogpi")
# win.geometry("200x200+200+200")



# EXTENDED 可以使ListBox支持shift和control
lb = tkinter.Listbox(win,selectmod=tkinter.EXTENDED)

for item in ["one","two","three","four","five","good","nice","cool","one","two","three","four","five","good","nice","cool"]:
    lb.insert(tkinter.END,item)

# 按住shift，可以实现连选
# 按住control，可以实现多选

# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.config(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
sc["command"]=lb.yview

win.mainloop()