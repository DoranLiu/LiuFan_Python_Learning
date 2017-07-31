'''
通常一开始时使用工厂方法，因为它更简单。
如果后来发现应用需要许多工厂方法，那么将创建 一系列对象的过程合并在一起更合理，从而最终引入抽象工厂。

抽象工厂有一个优点，在使用工厂方法时从用户视角通常是看不到的，那就是抽象工厂能够 通过改变激活的工厂方法动态地(运行时)改变应用行为。
一个经典例子是能够让用户在使用应 用时改变应用的观感，而不需要终止应用然后重新启动。

为演示抽象工厂模式，我将重新使用Python 3 Patterns & Idioms(Bruce Eckel著)一书中的一 个例子(请参考[Eckel08，第193页])，它是我个人最喜欢的例子之一。
想象一下，我们正在创 造一个游戏，或者想在应用中包含一个迷你游戏让用户娱乐娱乐。
我们希望至少包含两个游戏， 一个面向孩子，一个面向成人。
在运行时，基于用户输入，决定该创建哪个游戏并运行。游戏的 创建部分由一个抽象工厂维护。
从孩子的游戏说起，我们将该游戏命名为FrogWorld。主人公是一只青蛙，喜欢吃虫子。每个英雄都需要一个好名字，在我们的例子中，这个名字在运行时由用户给定。
方法 interact_with()用于描述青蛙与障碍物(比如，虫子、迷宫或其他青蛙)之间的交互，如下 所示。
'''

class Frog:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self,obstacle, obstacle.action()))

class Bug:

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    '''
    类FrogWorld是一个抽象工厂，其主要职责是创建游戏的主人公和障碍物。
    区分创建方法并使其名字通用(比如，make_character()和make_obstacle())，
    这让我们可以动态改变当前激活的工厂(也因此改变了当前激活的游戏)，而无需进行任何代码变更。
    在一门静态语言中， 抽象工厂是一个抽象类/接口，具备一些空方法，但在Python中无需如此，因为类型是在运行时检测的(请参考[Eckel08，第195页]和网页[t.cn/h47Rs9])。
    '''

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Frog World ———'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))


class Ork:

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World ------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    '''
    类GameEnvironment是我们游戏的主入口。
    它接受factory作为输入，用其创建游戏的世界。
    方法play()则会启动hero和obstacle之间的交互
    '''
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    '''
    函数validate_age()提示用户提供一个有效的年龄。
    如果年龄无效，则会返回一个元组， 其第一个元素设置为False。
    如果年龄没问题，元素的第一个元素则设置为True，第二个元素是用户提供的年龄。
    '''
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try again…".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()
