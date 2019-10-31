import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("dogpi")
# win.geometry("400x400+200+200")


tree = ttk.Treeview()
tree.pack()

# 添加一级树枝
treeF1 = tree.insert("",0,"中国",text="CHI",values="F1")
treeF2 = tree.insert("",1,"美国",text="USA",values="F2")
treeF3 = tree.insert("",2,"英国",text="ENG",values="F3")

# 添加二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",values="F1_1")
treeF1_2 = tree.insert(treeF1,1,"吉林",text="中国吉林",values="F1_2")
treeF1_3 = tree.insert(treeF1,2,"辽宁",text="中国辽宁",values="F1_3")

treeF2_1 = tree.insert(treeF2,0,"德克萨斯",text="美国德克萨斯",value="F2_1")
treeF2_2 = tree.insert(treeF2,1,"纽约",text="美国纽约",value="F2_2")

# 添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈尔滨",text="黑龙江哈尔滨",value="F1_1_1")

win.mainloop()