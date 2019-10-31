import csv

def readCsv(path):
    infoList=[]
    with open(path,"r") as fd:
        allFileInfo = csv.reader(fd)
        # print(allFileInfo)
        # < _csv.reader object at 0x0000000002157528 >
        for row in allFileInfo:
            infoList.append(row)
    return infoList

def writeCsv(path,data):
    with open(path,"w") as fd:
        writer = csv.writer(fd)
        for rowData in data:
            writer.writerow(rowData)

path = r"D:\PythonCode\StudyCode\004_自动化办公\test.csv"
info = readCsv(path)

path2 = r"D:\PythonCode\StudyCode\004_自动化办公\test2.csv"
data=[["1","2","3"],["4","5","6"],["7","8","9"]]
writeCsv(path2,data)