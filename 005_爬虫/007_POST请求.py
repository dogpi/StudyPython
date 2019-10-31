'''
特点：把参数进行打包，单独传送
优点：数量大，安全（当对服务器数据进行修改时建议使用POST）
缺点：速度慢
'''

import urllib.request
import urllib.parse
import ssl

url = r"https://www.douban.com"

# 将要发送的数据合成一个字典
# 字典的键的取值网址里找，一般为input标签的name属性的值

data = {
    "username":"a823435202@qq.com",
    "password":"woshiwuyuagng"
}

postData = urllib.parse.urlencode(data).encode("utf-8")

# 请求体
req = urllib.request.Request(url,data=postData)

req = urllib.request.Request(url)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")

context= ssl._create_unverified_context()

# 请求
response = urllib.request.urlopen(req,context=context)

data = response.read()

with open("dogpi.html","wb") as fd:
    fd.write(data)
