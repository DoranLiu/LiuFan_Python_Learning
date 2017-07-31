'''
Prototype Design Pattern 原型设计模式

帮助我们创建对象的克隆，其最简单的形式就是一个clone()函数，接受一个对象作为输入参数，返回输入对象的一个副本。
在Python中，这可以 使用copy.deepcopy()函数来完成。
来看一个例子，下面的代码中有两个类，A和B。
A是父类，B是衍生类/子类。
在主程序部分，我们创建一个类B的实例b，并使用deepcopy() 创建b的一个克隆c。
结果是所有成员都被复制到了克隆c，以下是代码演示。
'''
import copy


class A:

    def __init__(self):
        self.x = 18
        self.msg = 'Hello'


class B(A):

    def __init__(self):
        A.__init__(self)
        self.y = 34

    def __str__(self):
        return '{}, {}, {}'.format(self.x, self.msg, self.y)

if __name__ == '__main__':
    b = B()
    c = copy.deepcopy(b)
    print([str(i) for i in (b, c)])
    print([i for i in (b, c)])
    # 两个对象位于两个不同的内存地址(输出中的0x...部分)。这意味着两个对象是两个独立的副本。
