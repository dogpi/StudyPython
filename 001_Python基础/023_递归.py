'''
递归调用：
    一个函数调用自身，这种调用称为递归调用

    凡是循环能做的工作，递归都能实现


1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求这一次的结果

'''

# 输入一个数（大于1），求1+2+3...+n的和

def sum(n):
    sum = 0;
    for x in range(1,n+1):
        sum+=x;
    return sum;

res = sum(5);
print("sum =",res)

def sum_1(n):
    if n == 1:
        return 1;
    else:
        return n+sum(n-1);

print("sum_1 =",sum_1(5))