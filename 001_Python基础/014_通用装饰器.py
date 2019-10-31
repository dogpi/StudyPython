


def outer(func):
    def inner(*args,**keyargs):
        # 可接受任何参数
        # 要添加的功能
        print("******************")
        return func(*args,**keyargs)
    return inner


@outer
def say(name,age):
    print("my name is %s ,I am %d years old."%(name,age))

say("dogpi",24)