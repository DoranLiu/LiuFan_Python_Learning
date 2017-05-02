'''
如何实现属性可修改的函数装饰器？

实际案例

为分析程序内那些函数执行时间开销较大，我们定义一个带timeout参数的函数装饰器，装饰功能如下：

统计被装饰函数单词调用运行时间
时间大于参数timeout的，将此次函数调用记录到log日志中
运行时可修改timeout的值
解决方案

为包裹函数增加一个函数，用来修改闭包中使用的自由变量

在python3中使用nonlocal访问嵌套作用于中的变量引用
'''
from functools import wraps
import time
import logging
from random import randint
def warn(timeout):
    # timeout = [timeout]  # py2
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            used = time.time() - start
            if used > timeout:
                # if used > timeout:  # py2
                msg = '"%s": "%s" > "%s"' % (func.__name__, used, timeout)
                # msg = '"%s": "%s" > "%s"' % (func.__name__, used, timeout[0])  # py2
                logging.warn(msg)
            return res
        def setTimeout(k):
            nonlocal timeout
            timeout = k
            # timeout[0] = k  # py2
        wrapper.setTimeout = setTimeout
        return wrapper
    return decorator
@warn(1.5)
def test():
    print('In Tst')
    while randint(0, 1):
        time.sleep(0.5)
for _ in range(10):
    test()
test.setTimeout(1)
for _ in range(10):
    test()
