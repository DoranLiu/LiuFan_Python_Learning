'''
如何通过实例方法名字的字符串调用方法

实际案例

某项目中，我们的代码使用了三个不同库中的图形类:

Circle
Triangle
Rectangle
他们都有一个获取图形面积的接口，但接口名字不同，我们可以实现一个统一的获取面积的函数，使用没种方法名进行尝试，调用相应类的接口

解决方案

使用内置函数getattr，通过名字在实例上获取方法对象，然后调用；
使用标准库operator下的methodcaller函数调用；
'''

class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def get_area(self):
        return self.w * self.h
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        a, c, b = self.a, self.b, self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
def getArea(shape):
    for name in ('area', 'get_area', 'getArea'):
        f = getattr(shape, name, None)
        if f:
            return f()
shape1 = Circle(2)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(6, 4)
shapes = [shape1, shape2, shape3]
print(list(map(getArea, shapes)))

# 方法2
s = 'abc123abc456'
s.find('abc',4)
from operator import methodcaller
methodcaller('find','abc',4)(s)
