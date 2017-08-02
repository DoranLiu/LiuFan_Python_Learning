# coding: utf-8
'''
解释器(Interpreter)

对每个应用来说，至少有以下两种不同的用户分类。
 基本用户:这类用户只希望能够凭直觉使用应用。他们不喜欢花太多时间配置或学习应 用的内部。对他们来说，基本的用法就足够了。
 高级用户:这些用户，实际上通常是少数，不介意花费额外的时间学习如何使用应用的 高级特性。如果知道学会之后能得到以下好处，他们甚至会去学习一种配置(或脚本) 语言。

解释器(Interpreter)模式仅能引起应用的高级用户的兴趣。
这是因为解释器模式背后的主 要思想是让非初级用户和领域专家使用一门简单的语言来表达想法。
然而，什么是一种简单的语言对于我们的需求来说，一种简单的语言就是没编程语言那么复杂的语言。
'''
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Gate:

    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:

    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:

    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True

    def turn_off(self):
        print('turning off the aircondition')
        self.is_on = False


class Heating:

    def __init__(self):
        self.is_on = False

    def __str__(self):
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turning off the heating')
        self.is_on = False


class Boiler:

    def __init__(self):
        self.temperature = 83  # in celsius

    def __str__(self):
        return 'boiler temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the boiler's temperature by {} degrees".format(amount))
        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the boiler's temperature by {} degrees".format(amount))
        self.temperature -= amount


class Fridge:

    def __init__(self):
        self.temperature = 2  # 单位为摄氏度

    def __str__(self):
        return 'fridge temperature: {}'.format(self.temperature)

    def increase_temperature(self, amount):
        print("increasing the fridge's temperature by {} degrees".format(amount))
        self.temperature += amount

    def decrease_temperature(self, amount):
        print("decreasing the fridge's temperature by {} degrees".format(amount))
        self.temperature -= amount


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    tests = ('open -> gate',
             'close -> garage',
             'turn on -> aircondition',
             'turn off -> heating',
             'increase -> boiler temperature -> 5 degrees',
             'decrease -> fridge temperature -> 2 degrees')
    open_actions = {'gate': gate.open,
                    'garage': garage.open,
                    'aircondition': airco.turn_on,
                    'heating': heating.turn_on,
                    'boiler temperature': boiler.increase_temperature,
                    'fridge temperature': fridge.increase_temperature}
    close_actions = {'gate': gate.close,
                     'garage': garage.close,
                     'aircondition': airco.turn_off,
                     'heating': heating.turn_off,
                     'boiler temperature': boiler.decrease_temperature,
                     'fridge temperature': fridge.decrease_temperature}

    for t in tests:
        if len(event.parseString(t)) == 2:  # 没有参数
            cmd, dev = event.parseString(t)
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
            if 'open' in cmd_str or 'turn on' in cmd_str:
                open_actions[dev_str]()
            elif 'close' in cmd_str or 'turn off' in cmd_str:
                close_actions[dev_str]()
        elif len(event.parseString(t)) == 3:  # 有参数
            cmd, dev, arg = event.parseString(t)
            cmd_str, dev_str, arg_str = ' '.join(cmd), ' '.join(dev), ' '.join(arg)
            num_arg = 0
            try:
                num_arg = int(arg_str.split()[0])  # 抽取数值部分
            except ValueError as err:
                print("expected number but got: '{}'".format(arg_str[0]))
            if 'increase' in cmd_str and num_arg > 0:
                open_actions[dev_str](num_arg)
            elif 'decrease' in cmd_str and num_arg > 0:
                close_actions[dev_str](num_arg)

if __name__ == '__main__':
    main()
