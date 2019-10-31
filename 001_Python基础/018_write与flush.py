



path = "D:\PythonCode\StudyCode\File.txt"

fd = open(path,"w")
fd.write("dogpi is a good man")
# 刷新缓冲区，缓冲区中的内容会写入到文件
fd.flush()
fd.close()

fd = open(path,"a")
fd.write("\ncatpi is a good man")
fd.flush()
fd.close()