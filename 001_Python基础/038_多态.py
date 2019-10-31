'''
多态：一种事物的多种形态
'''

class Person(object):
    def __init__(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass

class Student(Person):
    def __init__(self):
        pass
    def eat(self):
        print("学生吃辣条")
        return "学生吃辣条"
    def work(self):
        print("学生学习")

class Worker(Person):
    def __init__(self):
        pass
    def eat(self):
        print("工人喝啤酒")
        return "工人喝啤酒"
    def work(self):
        print("工人有力量")


def bus(per):
    print("%s 坐汽车"%(per.eat()))

def main():
    s = Student()
    print(type(s))
    s.eat()
    s.work()

    w = Worker()
    print(type(w))
    w.eat()
    w.work()


    bus(s)
    bus(w)

if __name__ == '__main__':
    main()