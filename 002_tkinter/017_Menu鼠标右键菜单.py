import tkinter

win = tkinter.Tk()
win.title("dogpi")

menubar = tkinter.Menu(win)

menu1 = tkinter.Menu(menubar,tearoff=False)

for item in ["Python","C++","C","Java","Shell","quit"]:
    if item=="quit":
        # 添加分割线
        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=lambda:print("+++++++++"))

menubar.add_cascade(label="语言",menu=menu1)

def showMenu(event):
    menubar.post(event.x_root,event.y_root)


win.bind("<Button-3>", showMenu)
win.mainloop()