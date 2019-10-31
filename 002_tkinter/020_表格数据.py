import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
# win.geometry("400x400+200+200")


tree = ttk.Treeview(win)
tree.pack()
# 列
tree["columns"] = ("姓名","年龄","身高","体重")
tree.column("姓名",width=100)
tree.column("年龄",width=100)
tree.column("身高",width=100)
tree.column("体重",width=100)

# 设置表头
tree.heading("姓名",text="name")
tree.heading("年龄",text="age")
tree.heading("身高",text="height")
tree.heading("体重",text="weight")

# 添加数据
tree.insert("",0,text="line1",values=("武钰钢",25,170,160))
tree.insert("",1,text="line2",values=("武子昂",27,170,140))

win.mainloop()