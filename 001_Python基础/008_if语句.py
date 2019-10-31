
'''
if 表达式:
    语句

if 表达式:
    语句
else：
    语句

if 表达式:
    语句
elif 表达式:
    语句
else:
    语句
'''

'''
if 10 == 20:
    print("10 == 20")
else:
    print("10 != 20")

if 10 == 20:
    print("10 == 20")
elif 10 == 10:
    print("10 == 10")
else:
    print("false")
'''

'''
num = int(input())

if num % 2 == 0:
    print("是偶数")
else:
    print("是奇数")

if 0:
    print("000")

if 1:
    print("111")
'''

#  求输入的数是不是水仙花数

num = int(input("请输入一个三位数："))

a = num % 10        # 个位
b = num //10 % 10   # 十位
c = num // 100      # 百位

if num == a**3 + b**3 + c**3:
    print("水仙花数")
else:
    print("不是水仙花数")