import urllib.request

# 向指定的URL地址发送请求，并返回服务器响应的数据
response = urllib.request.urlopen("http://www.baidu.com")

'''
# 读取返回数据，读取网页的全部内容
data = response.read()
print(type(data))
print(data.decode("utf-8"))

# 将爬取的网页写入到文件
with open("baidu.html","wb") as fd:
    fd.write(data)
'''

# 读取一行
# data = response.readline()

# 读取所有行，以列表的形式返回每一行
data = response.readlines()
print(data)
print(type(data))
# 打印网页的第151行
print(data[150].decode("utf-8"))
print(type(data[150].decode("utf-8")))
print(len(data))


# response属性
# 返回单签环境有关信息
print(response.info())

# 返回状态码
print(response.getcode())
'''
if response.getode() == 200 or response.getcode()==304:
    pass
    # 返回200表示请求成功，进行操作
    # 304也是成功
'''

# 返回当前正在爬取的地址
print(response.geturl())

# URL参数编码
url = r"https://www.baidu.com/s?wd=%E5%8D%9A%E5%AE%A2%E5%9B%AD&rsv_spt=1&rsv_iqid=0xc6dba9590003de1f&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=48021271_10_hao_pg&rsv_enter=1&rsv_dl=ib&rsv_sug3=12&rsv_sug1=8&rsv_sug7=101&rsv_sug2=0&inputT=3856&rsv_sug4=4840"

# 解码
decodeUrl = urllib.request.unquote(url)
print(decodeUrl)

# 解码的url不可以用于请求
# response = urllib.request.urlopen(decodeUrl)
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-12: ordinal not in range(128)

# 编码
decodeUrl = "热门"
encodeUrl = urllib.request.quote(decodeUrl)
print(encodeUrl)

# 编码的URL也不可以用于请求，只有参数是编码的URL才可以用于请求，编码后的URL符号会被替换
# https%3A//www.baidu.com/s%3Fwd%3D%E5%8D%9A%E5%AE%A2%E5%9B%AD%26rsv_spt%3D1 编码
# https://www.baidu.com/s?wd=%E5%8D%9A%E5%AE%A2%E5%9B%AD&rsv_spt=1  只编码参数
# response= urllib.request.urlopen(encodeUrl)
# data = response.read().decode("utf-8")
# print(data)