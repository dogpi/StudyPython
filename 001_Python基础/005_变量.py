'''
查看变量的类型
查看变量的首地址
删除变量
'''
age = 18
age = 28


# 删除变量
# del age
# print(age)
'''
Traceback (most recent call last):
  File "/home/dog-pi/PycharmProjects/StudyCode/005_变量.py", line 6, in <module>
    print(age)
NameError: name 'age' is not defined
'''

# num1 = int(input("请输入一个数字："))
# num2 = int(input("请再输入一个数字"))
# print("num1 + num2 =",num1+num2)
'''
请输入一个数字：a
Traceback (most recent call last):
  File "/home/dog-pi/PycharmProjects/StudyCode/005_变量.py", line 13, in <module>
    num1 = int(input("请输入一个数字："))
ValueError: invalid literal for int() with base 10: 'a'
'''

# 查看变量的类型
print(type(age))
# <class 'int'>

age = 28.5
print(type(age))
# <class 'float'>

age = "good"
print(type(age))
# <class 'str'>

# 查看变量的首地址
print(id(age))
# 140462209833368