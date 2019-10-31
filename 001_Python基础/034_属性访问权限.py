class Person(object):
    # 构造函数
    def __init__(self, name, age, height, weight):
        self.name = name
        # 带双下划綫，表示私有属性
        # 在类的外部不能直接访问
        # Python的私有属性不是真正的私有属性
        # 在类的外部可以通过_Person__age的方式访问，不同的解释器可能不同
        # self.__age__不是私有属性，只有前面有两个下划线的才是私有属性
        # 前后都有两个下划线的称为特殊变量，如__init__，表示这种变量是特有的，一般都是系统所有
        #   _XXX 前面有一个下划线，外部可以访问，但是按照约定的规则，意思是“虽然可以被访问，
        #   但请把它当做为私有属性，不要在外部对它进行访问”
        self.__age = age
        self.height = height
        self.weight = weight
    def run(self):
        print(self.__age)
    def changeAge(self,age):
        self.__age = age;

per = Person('tom',18,180,140)
# 如果不希望内部属性在外部被直接访问，在属性前加__
per.__age = 1111  # 这个__age不是类的私有属性，而是动态添加的属性，如per.a = 10  print(per.a)
per.a = 11111
print(per.a)    # 11111
# AttributeError: 'Person' object has no attribute '__age'
# print(per.name,per.__age,per.weight,per.height)

# 可以通过类的内部函数调用或修改私有属性
per.run()
per.changeAge(20)
per.run()
# 强制访问私有属性，强烈不建议使用
print(per._Person__age)