# coding: utf-8


# LazyProperty类实际上是一个描述符(请参考网页[t.cn/RqrYBND])。
# 描述符(descriptor) 是Python中重写类属性访问方法(__get__()、__set__()和__delete__())的默认行为要使 用的一种推荐机制。
class LazyProperty:

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print('function overriden: {}'.format(self.method))
        # print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        # print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 代价大的
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 做更多的事情。。。
    print(t.resource)
    print(t.resource)

if __name__ == '__main__':
    main()
