# 有序字典
from collections import OrderedDict

# 读取数据
from pyexcel_xls import get_data,save_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()
    xdata = get_data(path)
    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

def makeExcelFile(path,data):
    dic = OrderedDict()
    for sheetName,sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)
    save_data(path,dic)


path = r"D:\PythonCode\StudyCode\004_自动化办公\test.xlsx"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))

toPath = r"D:\PythonCode\StudyCode\004_自动化办公\test_write.xls"
makeExcelFile(toPath,{"表1":[[1,2,3],[4,5,6],[7,8,9]],
                      "表2":[[1,2,3,4],[2,3,4,5],[3,4,5,6]]})