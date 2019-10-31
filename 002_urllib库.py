import urllib.request
import urllib.parse
'''
Python 内置的http请求库
urllib.request      请求模块
urllib.error        异常处理模块
urllib.parse        url解析模块
urllib.robotparser  robots.txt解析模块
'''

'''
发送request请求
urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
'''
# 只打开url
response_1 = urllib.request.urlopen("http://www.baidu.com")
with open("baidu.html","wb") as fd:
    fd.write(response_1.read())

# 向指定的服务器发送POST请求
data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding='utf-8')
response_2 = urllib.request.urlopen("http://www.httpbin.org/post",data=data)
with open("httpbin_hello.html","wb") as fd:
    fd.write(response_2.read())

# 设置超时时间
data = bytes(urllib.parse.urlencode({"word":"hello"}),encoding='utf-8')
try:
    response_3 = urllib.request.urlopen("http://www.httpbin.org/post",data=data,timeout=0.1)
except:
    print("timeout")
else:
    with open("httpbin_timeout.html","wb") as fd:
        fd.write(response_3.read())

# 响应
print(type(response_1))
print(response_1.status)                # 状态码
print(response_1.getheaders())          # 响应头
print(response_1.getheader("Server"))   # 响应头的指定字段

# request

request_1 = urllib.request.Request("http://www.baidu.com")
response = urllib.request.urlopen(request_1)
print(response.read().decode("utf-8"))
print("****************************************")


# Request
url = "http://httpbin.org/post"
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Host":"httpbin.org"
}
dict = {
    "name":"Germey"
}
data = bytes(urllib.parse.urlencode(dict),encoding="utf8")
req = urllib.request.Request(url=url,data=data,headers=header,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print("****************************************")


# add_header
req = urllib.request.Request(url=url,data=data,method="POST")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
print("****************************************")


# Handler

#代理
'''
proxy_handler = urllib.request.ProxyHandler({
    "http":"http://127.0.0.1:9743",
    "https":"https://127.0.0.1:9743"
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open("http://www.baidu.com")
print(response.read())
'''

# Cookie

import http.cookiejar
import urllib.request

# 获取cookie值
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name+"="+item.value)

# 保存cookie到本地文件
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)
# LWP格式保存cookie
filename = "cookie_LWP.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


# 从本地文件中加载cookie
cookie = http.cookiejar.LWPCookieJar()
cookie.load("cookie_LWP.txt",ignore_expires=True,ignore_discard=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))


# 异常处理
import urllib.error

try:
    response = urllib.request.urlopen("http://cuiqingcai.com/index.html")
except urllib.error.URLError as e:
    print(e.reason)
    # Not Found
else:
    print(response.read())

print("----------------------")

try:
    response = urllib.request.urlopen("http://cuiqingcai.com/index.html")
except  urllib.error.HTTPError as e:
    print(e.reason,e.code,e.headers,sep='\n')
except urllib.error.URLError as e:
    print(e.reason)
    # Not Found
else:
    print("Request Successfully")

print("----------------------")

import socket
try:
    response = urllib.request.urlopen("http://cuiqingcai.com/index.html",timeout=0.01)
except urllib.error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout):
        print("TIME OUT")
else:
    print(response.read())


# URL解析
# urlparse

# 把url拆分成六个部分
result = urllib.parse.urlparse("https://www.baidu.com/baidu?wd=%E7%8B%97%E5%B1%81&tn=monline_3_dg&ie=utf-8")
print(type(result),result)

result = urllib.parse.urlparse("www.baidu.com/baidu?wd=%E7%8B%97%E5%B1%81&tn=monline_3_dg&ie=utf-8",scheme="https")
print(type(result),result)

result = urllib.parse.urlparse("http://www.baidu.com/baidu?wd=%E7%8B%97%E5%B1%81&tn=monline_3_dg&ie=utf-8",scheme="https")
print(type(result),result)

# 把fragment拼接到query中，fragment置为空，如果query为空，则继续向前拼接
result = urllib.parse.urlparse("http://www.baidu.com/baidu?wd=%E7%8B%97%E5%B1%81&tn=monline_3_dg&ie=utf-8",allow_fragments=False)
print(type(result),result)


# urlunparse
data = ["http","www.baidu.com","index.html","user","a=6","comment"]
print(urllib.parse.urlunparse(data))


# urljoin
print(urllib.parse.urljoin("http://www.baidu.com","FAQ.html"))
# 使用后者的字段覆盖前者的字段，如果前面的字段在后面不存在，就用前面的字段补充
print(urllib.parse.urljoin("http://www.baidu.com","https://www.cuiqingcai.com/FAQ.html"))

# urlencode
params = {
    "name":"germey",
    "age":22
}
base_url = "http://www.baidu.com?"
url = base_url+urllib.parse.urlencode(params)
print(url)
