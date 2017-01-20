# 关于名称空间
# 1. dir
# 2. vars


#---------------------------------------------------------------
# 使用 dir 函数
# dir 返回由给定模块, 类, 实例, 或其他类型的所有成员组成的列表. 这可能在交互式 Python 解释器下很有用, 也可以用在其他地方.
def dump(value):
    print (value, "=>", dir(value))
import sys
dump(0)
dump(1.0)
dump(0.0j) # complex number
dump([]) # list
dump({}) # dictionary
dump("string")
dump(len) # function
dump(sys) # module
'''
eg:
0 => ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__',
'__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__',
'__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__',
'__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__',
 '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__',
'__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__',
 '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
'''

#---------------------------------------------------------------
# 使用 dir 函数查找类的所有成员
class A:
    def a(self):
        pass
    def b(self):
        pass

class B(A):
    def c(self):
        pass
    def d(self):
        pass

# getmember 函数返回给定类定义的所有类级别的属性和方法.
# getmembers 函数返回了一个有序列表. 成员在列表中名称出现的越早, 它所处的类层次就越高. 如果无所谓顺序的话, 可以使用字典代替列表.
def getmembers(klass, members=None):
    # get a list of all class members, ordered by class
    if members is None:
        members = []
    for k in klass.__bases__:
        getmembers(k, members)
    for m in dir(klass):
        if m not in members:
            members.append(m)
    return members

print (getmembers(A))
print (getmembers(B))
print (getmembers(IOError))
'''
['__doc__', '__module__', 'a', 'b']
['__doc__', '__module__', 'a', 'b', 'c', 'd']
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__dict__', '__getitem__', '__getslice__', '__setstate__', '__unicode__', 'args', 'message', 'errno', 'filename', 'strerror']
'''

#---------------------------------------------------------------
# 使用 vars 函数
# vars 函数与getmember相似, 它返回的是包含每个成员当前值的字典.
# 使用不带参数的 vars , 它将返回当前局部名称空间的可见元素(同 locals() 函数 ).
book = "library2"
scripts = 350
print ("the %(book)s book contains more than %(scripts)s scripts" % vars())
'''
the library2 book contains more than 350 scripts
'''









