# 检查对象类型
# 1. isinstance
# 2. callable
# 3. isinstance
# 4. issubclass


#---------------------------------------------------------------
# type 函数允许你检查一个变量的类型. 这个函数会返回一个 type descriptor (类型描述符) , 它对于 Python 解释器提供的每个类型都是不同的.

# Python 是一种动态类型语言, 这意味着给一个定变量名可以在不同的场合绑定到不同的类型上.
# example中将同样的函数分别被整数, 浮点数, 以及一个字符串调用:
def function(value):
    print (value)
function(1)
function(1.0)
function("one")

def dump(value):
    print (type(value), value)
dump(1)
dump(1.0)
dump("one")
'''
1
1.0
one
<type 'int'> 1
<type 'float'> 1.0
<type 'str'> one
'''

#---------------------------------------------------------------
# 每个类型都有一个对应的类型对象, 所以可以使用 is 操作符来检查类型.
def load(file):
    if isinstance(file, type("")):
        file = open(file, "rb")
    return file.read()
# print len(load("./samples/sample.jpg")), "bytes"
# print len(load(open("./samples/sample.jpg", "rb"))), "bytes"
'''
4672 bytes
4672 bytes
'''

#---------------------------------------------------------------
# callable 函数,可以检查一个对象是否是可调用的,无论是直接调用或是通过 apply.
# 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True.
def dump(function):
    if callable(function):
        print (function, "is callable")
    else:
        print (function, "is *not* callable")

class A:
    def method(self, value):
        return value
class B(A):
    def __call__(self, value):
        return value
a = A()
b = B()

dump(0) # simple objects
dump("string")
dump(callable)
dump(dump) # function
dump(A) # classes
dump(B)
dump(B.method)
dump(a) # instances
dump(b)
dump(b.method)
'''
0 is *not* callable
string is *not* callable
<built-in function callable> is callable
<function dump at 0x7fa42e07de60> is callable
__main__.A is callable
__main__.B is callable
<unbound method B.method> is callable
<__main__.A instance at 0x7fa42e07ba28> is *not* callable
<__main__.B instance at 0x7fa42e07ba70> is callable
<bound method B.method of <__main__.B instance at 0x7fa42e07ba70>> is callable
'''
# 类对象(A和B)都是可调用的;如果调用它们, 就产生新的对象(类实例). 但是 A 类的实例不可调用, 因为它的类没有实现 __call__ 方法.
# 可以在 operator 模块中找到检查对象是否为某一内建类型(数字, 序列, 或者字典等) 的函数.
# 但是, 因为创建一个类很简单(比如实现基本序列方法的类), 所以对这些类型使用显式的类型判断并不是好主意.
# 在处理类和实例的时候会复杂些. Python 不会把类作为本质上的类型对待;
# 相反地, 所有的类都属于一个特殊的类类型(special class type), 所有的类实例属于一个特殊的实例类型(special instance type).
# 这意味着你不能使用 type 函数来测试一个实例是否属于一个给定的类;
# 所有的实例都是同样的类型! 为了解决这个问题, 你可以使用 isinstance 函数,它会检查一个对象是不是给定类(或其子类)的实例.

#---------------------------------------------------------------
# 使用 isinstance 函数
class A:
    pass
class B:
    pass
class C(A):
    pass
class D(A, B):
    pass
def dump(object):
    print (object, "=>",)
    if isinstance(object,A):
        print ("A",)
    if isinstance(object,B):
        print ("B",)
    if isinstance(object,C):
        print ("C",)
    if isinstance(object,D):
        print ("D",)
    print
a = A()
b = B()
c = C()
d = D()
dump(a)
dump(b)
dump(c)
dump(d)
dump(0)
dump("string")
'''
<__main__.A instance at 0x7fa5a6bb7dd0> => A
<__main__.B instance at 0x7fa5a6bb7d40> => B
<__main__.C instance at 0x7fa5a6bb7d88> => A C
<__main__.D instance at 0x7fa5a6bb7e18> => A B D
0 =>
string =>
'''

#---------------------------------------------------------------
# issubclass 函数
# 与isinstance相似, 它用于检查一个类对象是否与给定类相同, 或者是给定类的子类.

# 注意, isinstance 可以接受任何对象作为参数, 而 issubclass 函数在接受非类对象参数时会引发 TypeError 异常.
print ('--------')

class A:
    pass
class B:
    pass
class C(A):
    pass
class D(A, B):
    pass
def dump(object):
    print (object, "=>",)
    if issubclass(object, A):
        print ("A"),
    if issubclass(object, B):
        print ("B"),
    if issubclass(object, C):
        print ("C"),
    if issubclass(object, D):
        print ("D"),
    print
dump(A)
dump(B)
dump(C)
dump(D)
dump(0)
dump("string")
'''
__main__.A => A
__main__.B => B
__main__.C => A C
__main__.D => A B D
0 =>Traceback (most recent call last):
  File "/home/ytroot/桌面/WorkSpaceLHW/ShoppingWebSpider/Python_learnning/1.核心模块/1.1.__builtin__/4-type-example.py", line 166, in <module>
    dump(0)
  File "/home/ytroot/桌面/WorkSpaceLHW/ShoppingWebSpider/Python_learnning/1.核心模块/1.1.__builtin__/4-type-example.py", line 153, in dump
    if issubclass(object, A):
TypeError: issubclass() arg 1 must be a class
'''
