import tkinter

win = tkinter.Tk()
win.title("dogpi")


'''
用户通过拖拽改变变量的值
'''

scale = tkinter.Scale(win,from_=0,to=99,orient=tkinter.VERTICAL)
scale.pack()

scale2 = tkinter.Scale(win,from_=0,to=100,orient=tkinter.HORIZONTAL,length=200,tickinterval=10)
scale2.pack()

def showNum():
    print(scale.get())

tkinter.Button(win,text="get",command=showNum).pack()

def setNum(x):
    scale2.set(x)

x=30
tkinter.Button(win,text="set",command=lambda :setNum(x)).pack()

win.mainloop()