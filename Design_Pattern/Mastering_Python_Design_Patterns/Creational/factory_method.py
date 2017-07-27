'''
创建者模式：
创建型设计模式处理对象创建相关的问题，目标是当直接创建对象不太方便时，提供更好的方式。
在工厂设计模式中，客户端可以请求一个对象，而无需知道这个对象来自哪里;也就是，使用哪个类来生成这个对象。

工厂背后的思想是简化对象的创建。
与客户端自己基于类实例化直接创建对象相比，基于一个中心化函数来实现，更易于追踪创建了哪些对象。
通过将创建对象的代码和使用对象的代码解耦，工厂能够降低应用维护的复杂度。

工厂通常有两种形式:
第一种是工厂方法(Factory Method)，它是一个方法(或以地道的Python 术语来说，是一个函数)，对不同的输入参数返回不同的对象;
第二种是抽象工厂，它是一组用于创建一系列相关事物对象的工厂方法。

创建者模式下有五种经典的模式：
1.抽象工厂模式 Abstract factory pattern, which provides an interface for creating related or dependent objects without specifying the objects' concrete classes.
2.生成器模式 Builder pattern, which separates the construction of a complex object from its representation so that the same construction process can create different representations.
3.工厂方法模式 Factory method pattern, which allows a class to defer instantiation to subclasses.
4.原型模式 Prototype pattern, which specifies the kind of object to create using a prototypical instance, and creates new objects by cloning this prototype.
5.单例模式 Singleton pattern, which ensures that a class only has one instance, and provides a global point of access to it.
'''

'''
工厂方法模式:
在工厂方法模式中，我们执行单个函数，传入一个参数(提供信息表明我们想要什么)，
但并不要求知道任何关于对象如何实现以及对象来自哪里的细节。

例如：
Django框架使用工厂方法模式来创建表单字段。
Django的forms模块支持不同种类字段 (CharField、EmailField)的创建和定制(max_length、required)。

应用：
如果因为应用创建对象的代码分布在多个不同的地方，而不是仅在一个函数/方法中，你发现没法跟踪这些对象，那么应该考虑使用工厂方法模式。
工厂方法集中地在一个地方创建对象，使对象跟踪变得更容易。
注意，创建多个工厂方法也完全没有问题，实践中通常也这么做，对相似的对象创建进行逻辑分组，每个工厂方法负责一个分组。
'''
import xml.etree.ElementTree as etree
import json


class JSONConnector:

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person',
                                                     'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']),
               p.text) for p in liar.find('phoneNumbers')]

    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()
