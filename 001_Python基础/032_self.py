'''
self代表类的实例，而不是类
哪个对象调用方法，那么self就代表哪个对象

self.__class__ 代表类名
'''

class Person(object):
    # 构造函数
    def __init__(self, name, age, height, weight):
        self.name = name        # self.name 表示具体实例的name
        self.age = age
        self.height = height
        self.weight = weight
    # 析构函数
    def __del__(self):
        print("析构函数")
    def say(self):
        print(self.name,self.age,self.height,self.weight)
    def run(self):
        print("run")
    def eat(self,food):
        print("eat",food)
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillEle(self):
        print("我已经把大=大象装进了冰箱")
    def closeDoor(self):
        print("我已经关闭冰箱门")
    def className(self):
        print(self.__class__)

per1 = Person('tom',18,180,140)
per1.say()
per1.className()

per2 = Person('joy',20,170,150)
per2.say()

per3 = Person('joy',20,170,150)
del per3