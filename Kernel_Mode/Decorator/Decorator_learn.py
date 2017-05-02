'''
https://blog.ansheng.me/article/advanced-python-intensive-training-of-advanced-decorator-tips/

装饰器：
定义装饰奇函数，用它来生成一个在原函数基础添加了新功能的函数，替代原函数

如有如下两道题：
题目一：
斐波那契数列又称黄金分割数列，指的是这样一个数列：1,1,2,3,5,8,13,21,….,这个数列从第三项开始，每一项都等于前两项之和，求数列第n项。

题目二：
一个共有10个台阶的楼梯，从下面走到上面，一次只能迈1-3个台阶，并且不能后退，走完整个楼梯共有多少种方法？
'''
# 函数装饰器
def memp(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

# 第一题
@memp
def fibonacci(n):
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print(fibonacci(30))

# 第二题
@memp
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count
print(climb(10, (1, 2, 3)))