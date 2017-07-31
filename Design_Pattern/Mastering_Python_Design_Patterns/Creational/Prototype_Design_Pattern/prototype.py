# coding: utf-8
'''
Prototype Design Pattern 原型设计模式

有时，我们需要原原本本地为对象创建一个副本。
举例来说，假设你想创建一个应用来存储、 分享、编辑(比如，修改、添加注释及删除)食谱。
用户Bob找到一份蛋糕食谱，在做了一些改 变后，觉得自己做的蛋糕非常美味，想要与朋友Alice分享这个食谱。
但是该如何分享食谱呢?
如果在与Alice分享之后，Bob想对食谱做进一步的试验，Alice手里的食谱也能跟着变化吗?
Bob能够持有蛋糕食谱的两个副本吗?
对蛋糕食谱进行的试验性变更不应该对原本美味蛋糕的食谱造成影响。

'''
import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        '''rest的例子有：出版商，长度，标签，出版日期'''
        self.name = name
        self.authors = authors
        self.price = price      # 单位为美元
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


'''
Prototype类在支持克隆之外做了一点更多的事情，
它包含了方法register()和unregister()，
这两个方法用于在一个字典中追 踪被克隆的对象。
注意这仅是一个方便之举，并非必需。
'''
class Prototype:

    def __init__(self):
        self.objects = dict()

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'), price=118, publisher='Prentice Hall',
              length=228, publication_date='1978-02-22', tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language(ANSI)', price=48.99,
                         length=274, publication_date='1988-04-01', edition=2)

    for i in (b1, b2):
        print(i)
    print('ID b1 : {} != ID b2 : {}'.format(id(b1), id(b2)))

if __name__ == '__main__':
    main()
