'''
如何在类中定义装饰器？

实际案例

实现一个能将函数调用信息记录到日志的装饰器：

把每次函数的调用时间，执行时间，调用次数写入日志
可以对被装饰函数分组，调用信息记录到不同日志
动态修改参数，比如日志格式
动态打开关闭日志输出功能
解决方案

为了让装饰器在使用上更加灵活，可以把类的实例方法作为装饰器，此时包裹函数中就可以持有实例对象，便于修改属性和扩展功能
'''
import logging
from time import localtime, time, strftime, sleep
from random import choice

class CallingInfo:
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')  # 日志保存的文件
        log.addHandler(fh)
        log.info('Start'.center(50, '-'))
        self.log = log
        self.formattter = '%(func)s -> [%(time)s - %(used)s - %(ncalls)s]'
    def info(self, func):
        def wrapper(*args, **kwargs):
            wrapper.ncalls += 1
            lt = localtime()
            start = time()
            res = func(*args, **kwargs)
            used = time() - start
            info = {}
            info['func'] = func.__name__
            info['time'] = strftime('%x %x', lt)
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formattter % info
            self.log.info(msg)
            return res
        wrapper.ncalls = 0
        return wrapper
    def SetFormatter(self, formatter):
        self.formattter = formatter
    def turnOm(self):
        self.log.setLevel(logging.INFO)
    def turnOff(self):
        self.log.setLevel(logging.WARN)
cinfo1 = CallingInfo('mylog1')
cinfo2 = CallingInfo('mylog2')
# 设置日志指定格式
# cinfo1.SetFormatter('%(func)s -> [%(time)s - %(ncalls)s]')
# 关闭日志
# cinfo2.turnOff()
@cinfo1.info
def f():
    print('in F')
@cinfo1.info
def g():
    print('in G')
@cinfo2.info
def h():
    print('in H')
for _ in range(50):
    choice([f, g, h])()
    sleep(choice([0.5, 1, 1.5]))