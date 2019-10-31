class Person(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money
    def run(self):
        print("run")
    def eat(self,food):
        print("eat ",food)
    def __private(self):
        print("base private function")

class Student(Person):
    def __init__(self,name,age,stuId,money):
        # 调用父类的构造函数
        super(Student,self).__init__(name,age,money)
        # Person.__init__(self,name,age,money)
        self.stuId = stuId
    def private_func(self):
        print("Public",self.age)
        # 子类无法访问父类的私有属性
        # print("Private",self.__money)
        print("Private",self._Person__money)
        self.eat("apple")
        # 子类无法调用父类的私有属性
        # self.__private()
        self._Person__private()

class Worker(Person):
    def __init__(self,name,age,money):
        super(Worker, self).__init__(name,age,money)
    # 函数重写
    def run(self):
        print("Worker run")

stu = Student("tom",18,10001,111)
print(stu.name,stu.age,stu.stuId)
stu.private_func()
stu.run()

wok = Worker("joy",20,3000)
wok.run()