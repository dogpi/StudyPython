import collections
import os

# 递归遍历目录结构
def getAllDir(path,sp = ""):
    fileList = os.listdir(path)
    # print(fileList)
    sp += "   "
    for fileName in fileList:
        # 判断是否是路径
        fileAbsPath = os.path.join(path,fileName)
        if os.path.isdir(fileAbsPath):
            print(sp+"dir:", fileName)
            getAllDir(fileAbsPath,sp)
        else:
            print(sp+"file:",fileName)

# 栈模拟递归调用，深度遍历
def getAllDirStack(path):
    stack = []
    stack.append(path)
    #  当栈为空时结束循环
    while len(stack):
        dirPath = stack.pop()
        fileList = os.listdir(dirPath)

        for fileName in fileList:
            absPath = os.path.join(dirPath,fileName)
            if os.path.isdir(absPath):
                print("dir:",fileName)
                stack.append(absPath)
            else:
                print("file:",fileName)

# 队列模拟，广度遍历
def getAllDirDeque(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue):
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            absPath = os.path.join(dirPath,fileName)
            if os.path.isdir(absPath):
                print("dir:",fileName)
                queue.append(absPath)
            else:
                print("file:",fileName)


# getAllDir(r"C:\Users\dog-pi\Desktop\OpenCV code")

# getAllDirStack(r"C:\Users\dog-pi\Desktop\OpenCV code")

# getAllDirDeque(r"C:\Users\dog-pi\Desktop\OpenCV code")

# 要对路径进行判断是不是目录
# getAllDir(r"C:\Users\dog-pi\Desktop\OpenCV code\opencv_002\opencv_002.sln")
