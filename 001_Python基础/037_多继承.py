class Father(object):
    def __init__(self,money):
        self.money = money
    def work(self):
        print("满头大汗")
    def play(self):
        print("开心")
    def eat(self):
        print("吃辣椒")

class Mother(object):
    def __init__(self,faceValue):
        self.faceValue = faceValue
    def cook(self):
        print("美味")
    def dress(self):
        print("漂亮")
    def eat(self):
        print("吃糖")

class Children(Father,Mother):
    def __init__(self,money,faceValue):
        Father.__init__(self,money)
        Mother.__init__(self,faceValue)
        # Father.money = money
        # Mother.faceValue = faceValue
    def printMoney(self):
        print(self.money)
    def prinFaceValue(self):
        print(self.faceValue)


def main():
    ch = Children(1000000000,9)
    ch.printMoney()
    ch.prinFaceValue()
    # 对于多继承中有相同函数，会继承列表中第一个字类的方法
    # 这里继承列表中第一个对象是Father，所以继承的是Father的eat()方法
    ch.eat()





if __name__ == "__main__":
    main()