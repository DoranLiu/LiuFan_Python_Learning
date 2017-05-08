'''
如何让类支持比较操作

实际案例
有时我们希望自定义类，实例间可以使用<、<=、>、>=、==、!=符号进行比较，我们自定义比较的行为，例如，有一个矩形的类，我们希望比较两个矩形的实例时，比较的是他们的面积.

解决方案
比较符号运算符重载，需要实现以下方法:__lt__，__le__，__gt__，__ge__，__eq__，__ne__，或者使用标准库下的functools下的类装饰器total_ordering可以简化此过程.
'''

from functools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class Shape(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def area(self):
        pass
    def __lt__(self, other):
        if not isinstance(other, Shape):
            raise TypeError('other not Shape')
        return self.area() < other.area()
    def __eq__(self, other):
        if not isinstance(other, Shape):
            raise TypeError('other not Shape')
        return self.area() == other.area()

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return self.r ** 2 * 3.14

r1 = Rectangle(5, 3)
r2 = Rectangle(5, 4)
c1 = Circle(3)
print(c1 <= r1)
print(r1 > c1)
print(r1 < r2)