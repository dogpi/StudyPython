'''
数字类型：
    整型
    浮点型
    复数

    1）整数
        Python的整型不区分short int long，统统当做int
        Python的整数可以使任意大小的值，包括负数
    2）浮点数
        浮点数由整数部分和小数部分组成
        浮点数运算可能会出现误差
    3）复数
        由实数部分和虚数部分组成
'''
import math
import random

num1 = 10
num2 = num1

# 连续定义多个变量
num5 = num4 = num3 = num2

print(num1,id(num1))
print(num2,id(num2))
print(num3,id(num3))
print(num4,id(num4))
print(num5,id(num5))
print("-"*15)
num1 = 20
print(num1,id(num1))
print(num2,id(num2))
print(num3,id(num3))
print(num4,id(num4))
print(num5,id(num5))
'''
10 10919616
10 10919616
10 10919616
10 10919616
10 10919616
---------------
20 10919936
10 10919616
10 10919616
10 10919616
10 10919616
'''

#
num6, num7 = 6, 7
print(num6,num7)

# 交换两个变量的值
num6, num7 = num7, num6
print(num6,num7)

# 浮点数误差
f1 = 1.1
f2 = 2.2
print(f1+f2)
# 3.3000000000000003

# 数字类型转换
# 浮点型转整型
print(int(1.1))
print(int(1.9))
# 整型转浮点型
print(float(1))
# 类型推导
print(1/2)

# 字符串转整型
print(int("123")+2)
print(float("12.5")+0.5)
print(int("+123")+2)
print(int("-123")+2)

# 数学函数
a1 = -10
print("a1的绝对值：",abs(a1))
a2 = abs(a1)
print(a2)

print((6>9)-(6<9))  # -1

a3 = 100
a4 = 10
print((a3>a4)-(a3<a4))  # a3>a4 返回1 a3<a4返回-1

print("最大值：",max(1,2,3,4,5,6,7))
print("最小值：",min(1,2,3,4,5,6,7))

# 指数运算 2^10=1024
print(pow(2,10))

# round 四舍五入
print(round(3.456))
print(round(3.567))

print(round(3.456,1))   # 保留小数点后1位
print(round(3.456,2))   # 保留小数点后2位


# 向上取整
print(math.ceil(18.1))
print(math.ceil(18.9))

# 向下取整
print(math.floor(18.1))
print(math.floor(18.9))

# 返回整数部分与小数部分
print(math.modf(22.4))
# (0.3999999999999986, 22.0)

# 开平方
print(math.sqrt(16))

# 随机数
# 1) 在指定的列表中随机选取
print(random.choice([1,3,5,"hello",7,9]))
# 2) range(5) [0,1,2,3,4]
print(random.choice(range(5)))
# 3) ["h","e","l","l","o"]
print(random.choice("hello"))
# 4) 产生1-100之间的随机数
print(random.choice(range(100))+1)
# 5) 范围[1-100) 步长为2 默认步长为1 [1,3,5,7...,99]
print(random.randrange(1,100,2))
print(random.randrange(1,100))
print(random.randrange(100))  # [0-99)
# 6) 随机生成[0,1)之间的数（浮点数）
print(random.random())
# 7) 给列表中的元素随机排序
list = [1,2,3,4,5]
random.shuffle(list)
print(list)
# 8) 随机生成一个实数[3-9]
print(random.uniform(3,9))