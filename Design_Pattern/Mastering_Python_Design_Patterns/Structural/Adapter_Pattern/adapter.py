'''
结构型设计模式处理一个系统中不同实体(比如，类和对象)之间的关系，关注的是提供一 种简单的对象组合方式来创造新功能(请参考[GOF95，第155页]和网页[t.cn/RqBdWzD])。

适配器模式(Adapter pattern)是一种结构型设计模式，帮助我们实现两个不兼容接口之间的兼容。
首先，解释一下不兼容接口的真正含义。如果我们希望把一个老组件用于一个新系统中，或者把一个新组件用于一个老系统中，不对代码进行任何修改两者就能够通信的情况很少见。
但又并非总是能修改代码，或因为我们无法访问这些代码(例如，组件以外部库的方式提供)，或因为修改代码本身就不切实际。
在这些情况下，我们可以编写一个额外的代码层，该代码层包含让两个接口之间能够通信需要进行的所有修改。
这个代码层就叫适配器。
'''
try:
    from external import Synthesizer, Human
except:
    from Design_Pattern.Mastering_Python_Design_Patterns.Structural.Adapter_Pattern.external import Synthesizer,Human

class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)
    # execute方法是计算机可以执行的主要动作。这一方法由客户端代码调用
    def execute(self):
        return 'executes a program'


'''
我们创建一个通用的Adapter类，将一些带不同接口的对象适配到一个统一接口中。 
__init__()方法的obj参数是我们想要适配的对象，adapted_methods是一个字典，键值对中的键是客户端要调用的方法，值是应该被调用的方法。'''
class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

'''
列表objects容纳着所有对象。属于Computer类的可兼 容对象不需要适配。可以直接将它们添加到列表中。不兼容的对象则不能直接添加。使用Adapter 类来适配它们。
'''
def main():
    # 直接使用computer调用
    objects = [Computer('Asus')]
    # 通过适配器调用
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))

    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))

if __name__ == "__main__":
    main()
