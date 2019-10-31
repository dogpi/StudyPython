import urllib.request
import ssl
import json

def ajaxCrawler(url):
    header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=header)
    context = ssl._create_unverified_context()
    # 使用ssl创建未验证的上下文
    response = urllib.request.urlopen(req,context=context)
    data = response.read()
    jsonStr = data.decode("utf-8")
    with open("douban.html","wb") as fd:
        fd.write(data)
    jsonData = json.loads(jsonStr)
    return jsonData



for i in range(1,11):
    # 豆瓣反爬虫
    url = "https://movie.douban.com/explore#!type=movie&tag=热门&sort=recommend&page_limit=20&page_start="+str(i*20)

    info = ajaxCrawler(url)
    print(info)