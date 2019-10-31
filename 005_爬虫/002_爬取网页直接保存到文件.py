import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",filename="baidu_a.html")

# urlretrieve在执行的过程中，会产生缓存
# 清理缓存
urllib.request.urlcleanup()