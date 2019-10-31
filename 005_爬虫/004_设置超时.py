import urllib.request


URL = r"http://www.baidu.com"

# 如果网页长时间未响应，系统判断超时，无法爬取

for i in range(1,100):
    try:
        response = urllib.request.urlopen(URL,timeout=0.1)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时")