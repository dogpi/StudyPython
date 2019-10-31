import os

'''
os：包含了普遍的操作系统的功能

'''

# 获取操作系统类型 nt--->Windows  posix--->Linux、Unix或MacOS
print(os.name)

# Linux环境下有效   操作系统详细信息
# print(os.uname())

# 环境变量
print(os.environ)
# 获取指定环境变量
print(os.environ.get("APPDATA"))

# 获取当前路径 .(相对路径)
print(os.curdir)

# 获取当前工作目录，即Python脚本所在的目录
print(os.getcwd())

# 以列表的形式返回指定目录下的所有文件
print(os.listdir("D:\PythonCode\StudyCode"))

# 创建新目录
os.mkdir("D:\PythonCode\StudyCode\dogpi")

# 删除目录
os.rmdir("D:\PythonCode\StudyCode\dogpi")

# 获取文件属性
print(os.stat("baidu.html"))

# 重命名
# os.rename("File.txt","File_bak.txt")

# 删除普通文件
# os.remove(path)

# 运行shell、cmd命令
# os.system("calc")

# 有些方法在os.path

# 查看当前的绝对路径
print(os.path.abspath("."))

# 拼接路径
p1 = r"D:\PythonCode"
p2 = r"StudyCode"
print(os.path.join(p1,p2))  # D:\PythonCode\StudyCode

p1 = r"D:\PythonCode"
p2 = r"\StudyCode"
print(os.path.join(p1,p2))  # D:\StudyCode 参数2开头不能有反斜杠

# 拆分路径
path = r"D:\PythonCode\StudyCode\baidu.html"
print(os.path.split(path))
# 拆分扩展名
print(os.path.splitext(path))

# 判断是不是目录
print(os.path.isdir(path))

# 判断目录是否存在
print(os.path.exists(path))

# 判断文件是否存在
print(os.path.isfile(path))

# 获取文件大小
print(os.path.getsize(path),"字节")

# 获取文件的目录
print(os.path.dirname(path))

# 获取文件名
print(os.path.basename(path))

