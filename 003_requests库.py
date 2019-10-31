import requests
'''
requests库是基于urllib实现的
'''

response = requests.get("http://www.baidu.com")
print("type(response)------->",type(response))
print("response.status_code->",response.status_code)
print("type(response.text)-->",type(response.text))
print("response.text-------->",response.text)
print("response.cookies----->",response.cookies)


requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")
requests.options("http://httpbin.org/get")

# GET
response = requests.get("http://httpbin.org/get")
print(response.text)

# 带参GET
import urllib.parse
data = {
    "name":"dogpi",
    "age":24
}
data_e = urllib.parse.urlencode(data)
url = "http://httpbin.org/get?"+data_e
response = requests.get(url)
print(response.text)