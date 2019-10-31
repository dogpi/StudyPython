import win32api
import win32con
import win32gui

def setWallPaper(path):
    # 打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)

    # 0 居中 2 拉伸 6 适应 10 填充
    win32api.RegSetValueEx(reg_key,"WallpaperStyle",0,win32con.REG_SZ,"2")


    # win32con.SPIF_SENDWININICHANGE 立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)


setWallPaper(r"D:\PythonCode\StudyCode\004_自动化办公\Tulips.jpg")