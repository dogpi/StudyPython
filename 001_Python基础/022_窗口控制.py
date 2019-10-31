import win32con
import win32gui
import time

QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")

while True:
    win32gui.ShowWindow(QQWin,win32con.SW_HIDE)
    time.sleep(1)
    win32gui.ShowWindow(QQWin,win32con.SW_SHOW)
    time.sleep(1)