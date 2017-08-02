'''
有时，我们希望在一个对象的状态改变时更新另外一组对象。在MVC模式中有这样一个非 常常见的例子，假设在两个视图(例如，一个饼图和一个电子表格)中使用同一个模型的数据，
无论何时更改了模型，都需要更新两个视图。这就是观察者设计模式要处理的问题(请参考[Eckel08，第213页])。

'''

'''
我们可以实现一个基类Publisher，包括添加、删除及通知观察者这些公用功能。
DefaultFormatter类继承自 Publisher，并添加格式化程序特定的功能。
我们可以按需动态地添加删除观察者。
'''
class Publisher:
    # 从Publisher类开始说起。观察者们保存在列表observers中。add()方法注册一个新的观察者，或者在该观察者已存在时引发一个错误。
    # remove()方法注销一个已有观察者，或者在该观察者尚未存在时引发一个错误。最后，notify()方法则在变化发生时通知所有观察者。
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add: {}'.format(observer))

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__,
                                                      publisher.name, hex(publisher.data)))


class BinaryFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__,
                                                      publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()
