'''
可以让我们以命令行的形式创建相关对象并设置任何属性。
'''
class Bunch(dict):
    def __init__(self,*args,**kwargs):
        super(Bunch,self).__init__(*args,**kwargs)
        self.__dict__=self


x = Bunch(name='bob',age='13')
print(x.name)
