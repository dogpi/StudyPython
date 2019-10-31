import datetime
'''
datetime比time高级，可以理解为datetime基于time进行了封装
提供了更为实用的函数，datetime提供的借口更直观，更容易调用

模块中的类：
    datetime        同时有时间和日期
    timedelta       主要用于计算时间的跨度
    tzinfo          时区相关
    time            只关注时间
    date            只关注日期
'''

d1 = datetime.datetime.now()
print(d1)
print(type(d1))

# 获取指定时间
d2 = datetime.datetime(1999,10,1,10,28,30,123456)
print(d2)

# 将时间转为字符串
d3 = d1.strftime("%y-%m-%d %H:%M:%S")
print(d3)
print(type(d3))
d4 = d1.strftime("%y-%m-%d %X")
print(d4)
print(type(d4))

# 将字符串转为datetime对象
d5 = datetime.datetime.strptime(d4,"%y-%m-%d %X")
print(d5)
print(type(d5))

d6 = datetime.datetime(1999,10,1,10,28,30,123456)
d7 = datetime.datetime.now()
d8 = d7-d6
print(d8)

