import sys
import importlib

importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPdf(path,toPath):
    # 以二进制形式打开文件
    fd = open(path,"rb")

    # 创建一个PDF文档分析器
    parser = PDFParser(fd)
    # 创建PDF文档
    pdfFile = PDFDocument()
    # 链接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    # 提供初始密码
    pdfFile.initialize()

    # 检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    # 数据管理器
    manager = PDFResourceManager()
    # 创建一个PDF设备对象
    laparams = LAParams()
    device = PDFPageAggregator(manager,laparams=laparams)
    # 解释器对象
    interpreter = PDFPageInterpreter(manager,device)

    # 开始循环，每次处理一页
    for pag in pdfFile.get_pages():
        interpreter.process_page(pag)
        layout = device.get_result()
        for x in layout:
            if (isinstance(x,LTTextBoxHorizontal)):
                with open(toPath,"a") as f:
                    str = x.get_text()
                    print(str)
                    f.write(str+"\n")



path = r"D:\PythonCode\StudyCode\004_自动化办公\pdf.pdf"
toPath = r"D:\PythonCode\StudyCode\004_自动化办公\pdf.txt"
readPdf(path,toPath)
