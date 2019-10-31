
import urllib.request
import gzip
from io import BytesIO

def Explorer_1():
    url = "http://www.baidu.com"
    # 模拟浏览器

    # 添加请求头
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    # 设置一个请求体
    req = urllib.request.Request(url,headers=headers)
    # 发起请求
    response = urllib.request.urlopen(req)

    # data = response.read().decode("utf-8")
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
    # 因为数据为压缩数据

    string = response.read()
    buff = BytesIO(string)
    fd = gzip.GzipFile(fileobj=buff)
    data = fd.read().decode("utf-8")

    print(data)

def Explorer_2():
    url = "http://www.baidu.com"
    agentStr = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    req = urllib.request.Request(url)
    req.add_header("User-Agent",agentStr)
    response = urllib.request.urlopen(req)

    # data = response.read().decode("utf-8")
    # UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start byte
    # 因为数据为压缩数据

    data = response.read()
    # buff = BytesIO(data)
    # fd = gzip.GzipFile(fileobj=buff)
    # string = fd.read().decode("utf-8")
    # print(string)

    print(data.decode("utf-8"))

if __name__ == "__main__":
    # Explorer_1()
    Explorer_2()