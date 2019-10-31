import tkinter

win = tkinter.Tk()
win.title("dogpi")
win.geometry("400x400+200+200")

'''
文本控件，用于显示文本
'''

text = tkinter.Text(win,width=30,height=4)
text.pack()
str='''I stand here today humbled by the task before us, grateful for the trust you have bestowed, mindful of the sacrifices borne by our ancestors. I thank President Bush for his service to our nation, as well as the generosity and cooperation he has shown throughout this transition.'''
text.insert(tkinter.INSERT,str)
win.mainloop()