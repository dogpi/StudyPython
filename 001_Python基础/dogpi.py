import os

DOGPI = "dogpi"

def SayDogpi():
    print("My name is dogpi")

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

print("++++++++++++++++++")

if __name__=="__main__":
    print("dogpi")