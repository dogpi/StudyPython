import tkinter

win = tkinter.Tk()
win.title("dogpi")

'''
顶层菜单
'''
menubar = tkinter.Menu(win)
win.config(menu=menubar)

menu1 = tkinter.Menu(menubar,tearoff=False)
for item in ["Python","C++","C","Java","Shell","quit"]:
    if item=="quit":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=lambda:print("+++++++++"))
menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="green")
menu2.add_command(label="blue")
menubar.add_cascade(label="语言",menu=menu1)
menubar.add_cascade(label="颜色",menu=menu2)

win.mainloop()