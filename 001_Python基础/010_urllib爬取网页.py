import urllib.request


def print_bai_du_1():
    response = urllib.request.urlopen("http://www.baidu.com")
    # string
    # data = response.read().decode("utf-8")

    # bytes
    data = response.read()
    print(type(data))
    with open("baidu.html","wb") as fd:
        fd.write(data)
    print(data)

def print_bai_du_2():
    response = urllib.request.urlopen("http://www.baidu.com")
    data = response.readlines()
    print(type(data))
    print(len(data))
    print(data)

def print_bai_du_3():
    response = urllib.request.urlopen("http://www.baidu.com")
    print(response.info())
    print(response.getcode())
    print(response.geturl())

    url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=%E5%8D%9A%E5%AE%A2%E5%9B%AD&oq=%25E5%259C%25A8%25E7%25BA%25BF%25E7%25BC%2596%25E7%25A8%258B%25E5%25AD%25A6%25E4%25B9%25A0&rsv_pq=8cfdf0e8005549b4&rsv_t=2a06tUPsXWQqPfu3WIto%2BxVvu6aCjSaAQ0i%2FyGJz8Q08m9AqWs6UKZKMd%2Fs&rqlang=cn&rsv_enter=0&rsv_dl=tb&inputT=2659&rsv_sug3=15&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&prefixsug=%25E5%258D%259A%25E5%25AE%25A2%25E5%259B%25AD&rsp=3&rsv_sug4=2659&rsv_sug=1"
    # 解码URL中特殊字符（包括汉字）
    newUrl1 = urllib.request.unquote(url)
    print(newUrl1)
    newUrl2 = urllib.request.quote(newUrl1)
    print(newUrl2)

def print_bai_du_4():
    # 直接将一个网页爬取
    # urlretrieve在执行的过程中会产生一些缓存
    urllib.request.urlretrieve("http://www.baidu.com","baidu02.html")
    # 清理缓存
    urllib.request.urlcleanup()
if __name__ == "__main__":
    print_bai_du_1()
    print("*"*20)
    print_bai_du_2()
    print("*" * 20)
    print_bai_du_3()
    print("*" * 20)
    print_bai_du_4()
    print("*" * 20)
