'''
try:
    语句块
except 异常 as e: （匹配异常）
    语句1
except 异常 as e:
    语句2
...
except 异常 as e:
    语句n
else: （未出现异常）
    语句
'''

# 1、捕获异常
try:
    # print(3/0)
    print(num)
except NameError as e:
    print("没有该变量")
except ZeroDivisionError as e:
    print("除数为零")
else:
    print("无异常")


# 2、多种异常
try:
    print(4/0)
except (NameError,ZeroDivisionError):
    print("出现了NameError或ZeroDivisionError ")
finally:
    print("finally总会执行")

print("*"*10)


# 3、不指定捕获的异常
try:
    print(4/0)
except:     # 不匹配任何错误码，会匹配所有的异常
    print("程序出现了异常")

def func1(num):
    print(1/num)
    print("-------------")   # 除零错误 该行不会执行
def func2(num):
    func1(num)

def main(num):
    func2(num)
try:
    main(0)
except ZeroDivisionError as e:
    print("----除零错误-----")