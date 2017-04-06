# # apply
# #---------------------------------------------------------------
# # Python允许实时地创建函数参数列表. 只要把所有的参数放入一个元组中,然后通过内建的 apply 函数调用函数.
'''
python3x，已经不支持了
apply(self.func,self.args)
改为self.func(*self.args)
'''
#
# def function(a, b):
#     print (a, b)
# apply(function, ("whither", "canada?"))
# apply(function, (1, 2 + 3))
# '''
# whither canada?
# 1 5
# '''
#
# #---------------------------------------------------------------
# # 使用 apply 函数传递关键字参数
# # 要想把关键字参数传递给一个函数, 可以将一个字典作为 apply 函数的第 3个参数.
# def function(a, b):
#     print (a, b)
# apply(function, ("crunchy", "frog"))
# apply(function, ("crunchy",), {"b": "frog"})
# apply(function, (), {"a": "crunchy", "b": "frog"})
# '''
# crunchy frog
# crunchy frog
# crunchy frog
# '''
#
# #---------------------------------------------------------------
# # 使用 apply 函数调用基类的构造函数
# # apply 函数的一个常见用法是把构造函数参数从子类传递到基类, 尤其是构造函数需要接受很多参数的时候.
# class Rectangle:
#     def __init__(self, color="white", width=10, height=10):
#         print "create a", color, self, "sized", width, "x", height
#
# class RoundedRectangle(Rectangle):
#     def __init__(self, **kw):
#         apply(Rectangle.__init__,(self,),kw)
#
# rect1 = Rectangle(color="green", height=100, width=100)
# rect2= RoundedRectangle(color="blue",height = 20)
# '''
# create a green <__main__.Rectangle instance at 0x7fcbf47dc998> sized 100 x 100
# create a blue <__main__.RoundedRectangle instance at 0x7fcbf47dc9e0> sized 10 x 20
# '''
#
