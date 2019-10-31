
# 不同的类型使用+会有不同的解释
print(1+2)          # 3
print("1"+"2")      # 12

class Num(object):
    def __init__(self,num):
        self.num = num
    # 运算符重载
    def __add__(self, other):
        # 返回一个对象
        return Num(self.num+other.num)
    # 打印对象显示对象的值
    def __str__(self):
        return "num = "+str(self.num)
num1 = Num(1)
num2 = Num(2)
print((num1+num2).num)