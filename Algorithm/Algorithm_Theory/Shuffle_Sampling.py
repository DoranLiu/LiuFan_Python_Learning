'''
随机抽样和洗牌
'''

class Foo:

    def pp1(self):
        print('pro')

    def pp2(self,value):
        print(value)

    def pp3(self):
        print('de')

    SpecialFields = property(fget=pp1,fset=pp2,fdel=pp3)

obj = Foo()
print(obj.pp)
obj.pp = 99
print(obj.pp)
del obj.pp
print(obj.pp)
