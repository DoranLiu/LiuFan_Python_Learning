'''
如何定义带参数的装饰器？
实现一个装饰器，它用来检查被装饰函数的参数类型，装饰器可以通过指定函数参数的类型，调用时如果检测出类型不匹配则抛出异常，比如调用时可以写成如下：

@typeassert(str, int, int)
def f(a, b, c):
   ......
或者

@typeassert(y=list)
def g(x, y):
   ......

解决方案：
提取函数签名：inspect.signature()
带参数的装饰器，也就是根据参数定制化一个装饰器，可以看成生产装饰器的工厂，美的调用typeassert，返回一个特定的装饰器，然后用他去装饰其他函数。
'''
from inspect import signature
def typeassery(*ty_args, **ty_kwargs):
    def decorator(func):
        # 获取到函数参数和类型之前的关系
        sig = signature(func)
        btypes = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        def wrapper(*args, **kwargs):
            for name, obj in sig.bind(*args, **kwargs).arguments.items():
                if name in btypes:
                    if not isinstance(obj, btypes[name]):
                        raise TypeError('"{}" must be "{}" '.format(name, btypes[name]))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@typeassery(int, str, list)
def f(a, b, c):
    print(a, b, c)
# 正确的
f(1, 'abc', [1, 2, 3])
# 错误的
f(1, 2, [1, 2, 3])
