

path = "D:\PythonCode\StudyCode\File.txt"

fd = open(path,"r")
str = fd.read()
fd.close()
print(str)

fd = open(path,"r")
fd.seek(6,0)
str = fd.read()
print(str)

print("------------------------")
with open(path,"r") as fd:
    str = fd.readline()
    str.strip('\n')
    print(str)
    while str:
        str = fd.readline()
        str.strip('\n')
        print(str)

print("------------------------")
with open(path,"r") as fd:
    for line in fd.readlines():
        print(line.split('\n')[0])
