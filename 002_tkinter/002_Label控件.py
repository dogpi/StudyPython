import tkinter

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

'''
Label:标签控件可以显示文本
'''


# win：父窗体
# text：显示的文本内容
# bg：背景色
# fg：字体颜色
# wraplength:最大长度后换行
# justify:换行后的对齐方式
label = tkinter.Label(win,
                      text = "dogpi is a good man",
                      bg="pink",
                      fg="red",
                      font=("黑体",20),
                      width=20,
                      height=1,
                      wraplength=100,
                      justify = "left",
                      anchor="center"
                      )
# 显示
label.pack()

win.mainloop()