import tkinter

win = tkinter.Tk()
win.title("dogpi")
win.geometry("200x200+200+200")

# 创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win,width=30,height=4)
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)

# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str='''I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.
I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.
I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.'''

text.insert(tkinter.INSERT,str)
win.mainloop()