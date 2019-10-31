import tkinter

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

# 绑定变量
lv = tkinter.StringVar()

# 与BROWSE类似，但是SINGLE不支持鼠标按下后拖动选中
lb = tkinter.Listbox(win,selectmod=tkinter.SINGLE,listvariable=lv)
lb.pack()

for item in ["one","two","three","four","five","good","nice","cool"]:
    lb.insert(tkinter.END,item)

# 打印选项
print(lv.get())

# 设置选项
# print(lv.set(("1","2","3")))

# 绑定事件
def myPrint(e):
    print(lb.get(lb.curselection()))
lb.bind("<Double-Button-1>",myPrint)

win.mainloop()