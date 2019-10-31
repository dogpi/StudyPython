class Person(object):
    def __init__(self,age):
        self.__age = age
    '''
    def getAge(self):
        return self.__age
    def setAge(self,age):
        if age <0:
            age=0
        self.__age = age
    '''
    # property:可以对受限制的属性使用点语法
    # f方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    @age.setter    # 去掉双下划线.setter
    def age(self,age):
        if age<0:
            age = 0
        self.__age = age
per = Person(18)

# 属性直接对外暴露
# 不安全，没有数据过滤
# per.age = 0
# print(per.age)

# 使用限制访问，需要自己写set和get方法才能访问
# print(per.getAge())
# per.setAge(12)
# print(per.getAge())

per.age = 100   # 相当于调用了per.age(100)
print(per.age)  # 相当于调用了per.age()