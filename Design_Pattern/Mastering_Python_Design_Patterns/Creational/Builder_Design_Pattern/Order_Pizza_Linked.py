# coding: utf-8
'''
程序仅支持两种比萨类型是挺丢脸的。权衡利弊之 后考虑一下是否使用继承。
看看典型夏威夷比萨的原料，再决定通过扩展哪个类来实现: MargaritaBuilder 或 CreamyBaconBuilder ? 或 许 两 者 皆 扩 展 ( 请 参 考 网 页 [ t.cn/RqBr- XK5])?

在Effective Java (2nd edition)一书中，Joshua Bloch描述了一种有趣的建造者模式变体，
这种变体会链式地调用建造者方法，通过将建造者本身定义为内部类并从其每个设置器方法返回自身 来实现。
方法build()返回最终的对象。这个模式被称为流利的建造者。以下是其Python实现， 由本书的一位评审人友情提供。
'''

class Pizza:

    def __init__(self, builder):
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self):
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = ('Garlic: {}'.format(garlic), 'Extra cheese: {}'.format(cheese))
        return '\n'.join(info)

    class PizzaBuilder:

        def __init__(self):
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
    print(pizza)
