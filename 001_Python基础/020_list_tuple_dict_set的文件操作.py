import pickle  # 数据持久性模块

myList = [1,2,3,4,5,"dogpi is a good man"]

path = r"D:\PythonCode\StudyCode\FileOne.txt"

fd = open(path,"wb")
pickle.dump(myList,fd)
fd.close()

fd = open(path,"rb")
tempList = pickle.load(fd)
print(tempList)
fd.close()