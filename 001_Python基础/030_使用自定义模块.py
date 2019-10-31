# 一个py文件就是一个模块
# 如果模块中有可执行语句，在import时会执行，import相当于把引入的模块中的代码添加到import的位置，可通过__name__屏蔽不想要被引用的内容


# 1、导入模块中所有内容
# 同级目录下直接导入
import dogpi
# 会执行dogpi模块中的print("++++++++++++++++++")


# 2、导入指定的内容
# 只引用getAllDir方法和DOGPI常量
from dogpi import getAllDir,DOGPI


# dogpi.SayDogpi()

# dogpi.getAllDir(r"C:\Users\dog-pi\Desktop\OpenCV code")
getAllDir(r"C:\Users\dog-pi\Desktop\OpenCV code")

# print(dogpi.DOGPI)
print(DOGPI)

# 3、导入模块中所有的内容
from dogpi import *

SayDogpi()

# 4、给导入的方法重命名
from dogpi import SayDogpi as say

say()

