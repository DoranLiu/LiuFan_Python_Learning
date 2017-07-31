# coding: utf-8
'''
无论何时我们想对一个对象添加额外的功能，都有下面这些不同的可选方法。
 如果合理，可以直接将功能添加到对象所属的类(例如，添加一个新的方法)
 使用组合
 使用继承
与继承相比，通常应该优先选择组合，因为继承使得代码更难复用，继承关系是静态的，并且应用于整个类以及这个类的所有实例(请参考[GOF95，第31页]和网页[t.cn/RqrC8Yo])。
设计模式为我们提供第四种可选方法，以支持动态地(运行时)扩展一个对象的功能，这种方法就是修饰器。
修饰器(Decorator)模式能够以透明的方式(不会影响其他对象)动态地将功 能添加到一个对象中(请参考[GOF95，第196页])。
在许多编程语言中，使用子类化(继承)来实现修饰器模式(请参考[GOF95，第198页])。
在Python中，我们可以(并且应该)使用内置的修饰器特性。一个Python修饰器就是对Python语法的一个特定改变，用于扩展一个类、方法或函数的行为，而无需使用继承。
从实现的角度来说，Python修饰器是一个可调用对象(函数、方法、类)，接受一个函数对象fin作为输入，并返回另一个函数对象fout ( 请 参 考 网 页 https://pythonconquerstheuniverse.wordpress.com/2012/04/29/ python-decorators/)。
这意味着可以将任何具有这些属性的可调用对象当作一个修饰器。
修饰器模式和Python修饰器之间并不是一对一的等价关系。
Python修饰器能做的实际上比修 饰器模式多得多，其中之一就是实现修饰器模式(请参考[Eckel08，第59页]和网页[t.cn/RqrlLcQ])。
'''

import functools

'''
这个修饰器接受一个需要使用memoization的函数fn作为输入，使用一个名为known的dict作为缓存。
函数functools.wraps() 是一个为创建修饰器提供便利的函数;虽不强制，但推荐使用，因为它能保留被修饰函数的文档1和签名(请参考网页[t.cn/Rqrl0K5])。
这种情况要求参数列表*args，因为被修饰的函数可能有输入参数。
如果fibonacci()和nsum()不需要任何参数，那么使用*args确实是多余的，但它们是需要参数n的。
'''
def memoize(fn):
    known = dict()
    # 所有递归函数都能因memoization而提速，那么来试试常用的斐波那契数列例子。
    @functools.wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer

@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    from timeit import Timer

    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci','func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum','func': nsum}]

    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import {}'.format(m['import']))

        print('name: {}, doc: {}, executing: {}, time: {}'.format(m['func'].__name__, m['func'].__doc__,m['exec'], t.timeit()))
