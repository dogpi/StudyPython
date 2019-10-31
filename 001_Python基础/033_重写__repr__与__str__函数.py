'''
重写：将函数重新定义

__str__()
__repr__()
'''

class Person(object):
    # 构造函数
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __str__(self):
        # print(per)
        # 打印对象时自动调用
        # 是一个描述对象的方法
        return "str"
    def __repr__(self):
        # 没有__str__()时调用该函数
        # 在解释器总直接输入对象时调用该方法
        # >>>per = Person('tom', 18, 180, 140)
        # >>>per
        # repr
        # >>>print(per)
        # str
        return "repr"

per = Person('tom',18,180,140)
# 打印类的属性
# 如果属性特别多，手动输出的话很麻烦
print(per.name,per.age,per.weight,per.height)

print(per)
# <__main__.Person object at 0x00000000023E1518>