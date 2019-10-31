
# object:基类，超类，所有类的父类
class Person(object):
    # 定义属性
    # name = ""
    # age = 0
    # height = 0
    # weight = 0
    '''
    构造函数：
        在创建对象时自动调用
    '''
    def __init__(self, name, age, height, weight):
        print("__init__")
        print(name, age, height, weight)
        self.name = name        # self.name 表示具体实例的name
        self.age = age
        self.height = height
        self.weight = weight
    # 析构函数
    # 对象释放时自动调用
    def __del__(self):
        print("析构函数")
    #定义方法
    # 方法的第一个参数必须是self
    # self代表类的实例（某个对象）
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




'''
实例化对象
格式：对象名 = 类名（参数列表）
'''
'''
# 实例化一个对象
per1 = Person()
print(per1)
print(type(per1))

per2 = Person()
print(per2)
print(type(per2))

# 设置属性
per1.name = "tom"
per1.age = 18
per1.height = 180
per1.weight = 140
print(per1.name,per1.age,per1.height,per1.weight)

# 调用方法
per1.openDoor()
per1.fillEle()
per1.closeDoor()
per1.eat("apple")
'''

per = Person("tom",18,180,140)
# 手动释放对象，调用该对象的析构函数
del per