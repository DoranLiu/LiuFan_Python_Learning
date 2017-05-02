'''
如何为被装饰的函数保存元数据？

在函数对象张保存着一些函数的元数据，例如：

方法	描述
f.__name__	函数的名字
f.__doc__	函数文档字符串
f.__module__	函数所属模块名
f.__dict__	属性字典
f.__defaults__	默认参数元素

我们在使用装饰器后，再使用上面的这些属性访问时，看到的是内部包裹函数的元数据，原来函数的元数据变丢失掉了，应该如何解决？

解决方案:
使用标准库functools中的装饰器wraps装饰内部包裹函数，可以指定将原来函数的某些属性更新到包裹函数上面
'''

from functools import wraps

def mydecoratot(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper function"""
        print("In wrapper")
        func(*args, **kwargs)
    return wrapper

@mydecoratot
def example():
    """example function"""
    print('In example')
print(example.__name__)
print(example.__doc__)