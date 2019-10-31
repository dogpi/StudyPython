import functools


print(int("1010",base=2))

print(int("1010",base=10))

def int2(str,base=2):
    return int(str,base)

print(int2("1010"))

# 把一个可变参数固定，形成一个新的函数
int3 = functools.partial(int,base = 2)
print(int3("111"))