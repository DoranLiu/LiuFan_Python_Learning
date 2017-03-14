"""
类型：
    函数装饰器，类装饰器，带参数的函数装饰器，带参数带类装饰器，为函数中和类中的方法添加装饰器
"""
# -----------------------------------------
"""
函数装饰器
"""
def decorator(func):
    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped
@decorator
def func(a, b):
    return a + b
print(func(1, 2))

# -----------------------------------------
"""
类装饰器
"""
class decorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
@decorator
def func(a, b):
    return a + b
print(func(1, 2))

# -----------------------------------------
"""
带参数的函数装饰器
"""
def parameter(a, b):
    print(a, b)
    def decorator(func):
        def wrapped(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapped
    return decorator
@parameter(1, 2)
def func(a, b):
    return a + b
print(func(10, 20))

# -----------------------------------------
"""
带参数的类装饰器
"""
def parameter(a, b):
    print(a + b)
    class decorator:
        def __init__(self, func):
            self.func = func
        def __call__(self, *args, **kwargs):
            return self.func(*args, **kwargs)
    return decorator
@parameter(1, 2)
def func(a, b):
    return a + b
print(func(10, 20))

# -----------------------------------------
"""
带参数的类装饰器
"""
def parameter(a, b):
    print(a, b)
    def decorator(cls):
        class wrapped:
            def __init__(self, *args, **kwargs):
                self.cls = cls(*args, **kwargs)
            def __getattr__(self, item):
                return getattr(self.cls, item)
        return wrapped
    return decorator
@parameter(1, 2)
class CLS:
    def __init__(self):
        self.a = 'a'
    def P(self, v):
        print(v)
obj = CLS()
print(obj.a)
obj.P('Hello,')

# -----------------------------------------
"""
为函数中和类中的方法添加装饰器
"""
def Call(aClass):
    calls = 0
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return aClass(*args, **kwargs)
    return onCall
@Call
def func(a, b):
    return a + b
print(func(1, 2))
class CLS:
    def __init__(self):
        self.a = 'a'
    @Call
    def b(self):
        return self.a
obj = CLS()
print(obj.b())