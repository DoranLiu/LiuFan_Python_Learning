'''
单例模式中，只会创建一次实例:
单例模式的实现只需要找一个变量存放创建的实例，
然后每次获取实例时，先检查变量中是否已保存实例，
如果没有则创建一个实例并将其存放到变量中，
以后都从这个变量中获取实例就可以了。
'''

'''--------------------------------------------------------------'''
# 1.使用__new__方法
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class MyClass(Singleton):
    a = 1

'''--------------------------------------------------------------'''
# 2.共享属性
# 创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
class Borg(object):
    _instance = {}
    def __new__(cls, *args, **kw):
        obj = super(Borg, cls).__new__(cls, *args, **kw)
        obj.__dict__ = cls._instance
        return obj

class MyClass2(Borg):
    a = 1

'''--------------------------------------------------------------'''
# 3.装饰器版本1
def singleton(cls, *args, **kw):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class MyClass:
  pass

# 3.装饰器版本2
class Singleton:
    """ 单例类装饰器，可以用于想实现单例的任何类。注意，不能用于多线程环境。 """
    def __init__(self, cls):
        """ 需要的参数是一个类 """
        self._cls = cls
    def Instance(self):
        """ 返回真正的实例 """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')
    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
# 装饰器
@Singleton
class A:
    """一个需要单列模式的类"""
    def __init__(self): pass
    def display(self):
        return id(self)

'''--------------------------------------------------------------'''
# 4.import方法
# 作为python的模块是天然的单例模式
'''mysingleton.py'''
class My_Singleton(object):
    def foo(self):
        pass
my_singleton = My_Singleton()

# to use
'''from mysingleton import my_singleton'''
my_singleton.foo()

'''--------------------------------------------------------------'''
# Singleton._instance 来存储创建的实例，并且保证只会创建一次实例。由于 Python 是一门动态语言，我们可以在运行时改变类定义。上面的代码中，我们在首次初始化 Singleton 时，我们将首次生成类 _A 的实例，并将其存储到 Singleton._instance 中，以后每次初始化 Singleton 时都从 Singleton._instance 获取真正干活的实例，这样我们就实现了单例模
class Singleton(object):
    class _A(object):
        """ 真正干活的类, 对外隐藏 """
        def __init__(self):
            pass
        def display(self):
            """ 返回当前实例的 ID，是全局唯一的"""
            return id(self)
    # 类变量，用于存储 _A 的实例
    _instance = None
    def __init__(self):
        """ 先判断类变量中是否已经保存了 _A 的实例，如果没有则创建一个后返回"""
        if Singleton._instance is None:
            Singleton._instance = Singleton._A()
    def __getattr__(self, attr):
        """ 所有的属性都应该直接从 Singleton._instance 获取"""
        return getattr(self._instance, attr)



'''
实例：使用单例模式连接数据库
'''
import sqlite3
from flask import current_app
from flask import _app_ctx_stack as stack
class SQLite3(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    def init_app(self, app):
        """ 典型的 Flask 扩展的初始化方式"""
        app.config.setdefault('SQLITE3_DATABASE', ':memory:')
        app.teardown_appcontext(self.teardown)
    def connect(self):
        """ 连接到 sqlite 数据库"""
        return sqlite3.connect(current_app.config['SQLITE3_DATABASE'])
    def teardown(self, exception):
        """ 关闭 sqlite 链接"""
        ctx = stack.top
        if hasattr(ctx, 'sqlite3_db'):
            ctx.sqlite3_db.close()
    @property
    def connection(self):
        """ 单例模式在这里：使用 flask._app_ctx_stack 存放 sqlite 链接, 每次获取数据库链接时都通过 connection 获取"""
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'sqlite3_db'):
                ctx.sqlite3_db = self.connect()
                return ctx.sqlite3_db
# 在以上的代码中，我们每次使用数据库的时候通过 SQLite3.connection 获取数据库连接就可以了。SQLite3.connection保证了数据库连接只会发生一次，其原理和之前我们实现单例模式的方式相同，只不过这里存储实例的地方变成 flask._app_ctx_stack了。

