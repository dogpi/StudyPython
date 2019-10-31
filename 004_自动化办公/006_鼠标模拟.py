import win32api
import win32con
import time

win32api.SetCursorPos([150,15])
time.sleep(0.1)

# 鼠标左键双击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)

# 拖拽
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
# win32api.SetCursorPos([155,100])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)