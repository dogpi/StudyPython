from types import MethodType

class Person(object):
    # 该类的对象可添加的属性
    # 用于限制添加属性
    __slots__ = ("name","age","speak")
    pass

per = Person()

# 动态添加属性，这就是动态语言的特点
per.name = "tom"
print(per.name)

# 只是给对象添加了一个新的属性，这个属性指向函数的地址，加上括号后可以执行
def say():
    print("dogpi is a good main")

per.speak = say
print("------")
per.speak()

# 给对象添加方法，
def say(self):
    print("dogpi is a good main "+self.name)
per.speak = MethodType(say,per)
per.speak()

# AttributeError: 'Person' object has no attribute 'height'
# per.height = 100