import tkinter
import time

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

'''
列表框，可以包含一个或多个文本框
'''
# 1、创建一个ListBox
lb = tkinter.Listbox(win,selectmod=tkinter.BROWSE)
lb.pack()

for item in ["good","nice","hello"]:
    # 在尾部添加
    lb.insert(tkinter.END,item)
# 在头部添加
lb.insert(tkinter.ACTIVE,"cool")
# 将列表总的元素添加到列表框
# lb.insert(tkinter.END,["good","nice","hello"])

# 删除
# 删除1-3
# lb.delete(1,3)
# 删除0
# lb.delete(0)

# 获取列表中的元素的个数
print(lb.size())

# 获取列表中元素的值
print(lb.get(0,2))

# 选中
lb.select_set(0,2)
lb.select_set(3)

# 返回当前选中的序号
print(lb.curselection())

# 判断一个选项是否被选中
print(lb.select_includes(1))
print(lb.select_includes(3))

# 取消选中
lb.select_clear(0,2)
lb.select_clear(3)



win.mainloop()