'''
概念：
    是一个闭包，把一个函数当做参数返回给一个替代版的函数，本质上就是一个返回函数的函数

    给函数增加一些功能
'''


# 简单的装饰器

def func1():
    print("dogpi is a good man")

'''
def outer():
    print("*************")
    func1()
'''


# 相当于给函数传入一个函数指针做参数，传出一个函数指针作为返回值，加上（）就是调用函数
def outer(func):
    def inner():
        print("*************")
        func()
    return inner

# f就是函数指针
f = outer(func1)
f()


outer()