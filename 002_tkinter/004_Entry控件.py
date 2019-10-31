import tkinter

def getStr():
    print(e.get())

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

'''
用于显示简单的文本内容
'''

# 绑定变量
e = tkinter.Variable()
entry = tkinter.Entry(win,textvariable=e)
# 给输入框赋值
e.set("haha")
entry.pack()

button = tkinter.Button(win,text = "get",command=getStr)
button.pack()



# 密文显示
entry2 = tkinter.Entry(win,show="*")
entry2.pack()



win.mainloop()