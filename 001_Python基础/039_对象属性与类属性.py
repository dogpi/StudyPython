class Person(object):
    # 类属性，使用类名来调用
    # 相当去C++中的静态属性
    name = "person"
    age = 0
    def __init__(self,name):
        # 对象属性
        # 对象调用属性时优先调用对象属性，对象属性中没有该属性就调用类属性
        self.name = name

print(Person.name,Person.age)
per = Person("tom")
print(per.name)
print(Person.name)
# 可以给对象属性动态的添加属性
per.money = 11111111
print(per.money)

# 删除对象属性后会调用类属性
del per.name
print(per.name)