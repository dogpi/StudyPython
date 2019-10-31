import urllib.request

url = "http://www.baidu.com"

# 请求头是字典格式
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}

# 设置一个请求体
req = urllib.request.Request(url,headers=header)

# req = urllib.request.Request(url)
# req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36")

# 发送请求体
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)