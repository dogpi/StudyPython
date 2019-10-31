import win32com
import win32com.client
import os

def readWorldFile(path):
    # 调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    # 打开文件
    doc = mw.Documents.Open(path)
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text
        print(line)
    doc.Close()
    mw.Quit()

def saveWordFile(path,toPath):
    # 另存为
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)
    # 2表示为TXT文件
    # 将word中的数据保存到另一个文件中
    doc.SaveAs(toPath,2)
    doc.Close()
    mw.Quit()

def createWordFile(path,name):
    word = win32com.client.Dispatch("Word.Application")

    #让文档可见
    word.Visible = True
    # 创建文旦
    doc = word.Documents.Add()

    # 写内容
    # 从头开始写
    r = doc.Range(0,0)
    r.InsertAfter("你好"+name+"\n")
    r.InsertAfter("       .....\n")
    # 存储文档
    doc.SaveAs(path)
    doc.Close()
    word.Quit()


path = r"D:\PythonCode\StudyCode\004_自动化办公\dogpi.doc"
toPath = r"D:\PythonCode\StudyCode\004_自动化办公\dogpi001.txt"
readWorldFile(path)
saveWordFile(path,toPath)



fileName = ["dogpi002","dogpi003","dogpi004"]
for name in fileName:
    path = os.path.join(os.getcwd(),name)
    createWordFile(path,name)