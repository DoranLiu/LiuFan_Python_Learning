'''
如何为创建大量实例节省内存

某网络游戏中，定义了玩家类Player(id,name,status,…)，每有一个在线玩家，在服务器程序内侧有一个Player的实例，当在线人数很多时，将产生大量实例(数百万级)
如何降低这些大量实例的内存开销？

解决方案
定义类的__slots__属性，它是用来声明实例属性名字的列表。
'''

class Plater:
    """ 关闭了动态绑定类属性的__dict__，以便节省内存，__dict__默认占用1024个字节 """
    __slots__ = ['uid', 'name', 'status', 'level']  # 声明实例拥有的属性，阻止动态属性绑定
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level

