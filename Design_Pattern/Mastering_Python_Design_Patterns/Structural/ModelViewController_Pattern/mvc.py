'''
Model-View-Controller

关注点分离(Separation of Concerns，SoC)原则是软件工程相关的设计原则之一。
SoC原则 背后的思想是将一个应用切分成不同的部分，每个部分解决一个单独的关注点。
分层设计中的层次(数据访问层、业务逻辑层和表示层等)即是关注点的例子。
使用SoC原则能简化软件应用的 开发和维护(请参考网页[t.cn/RqrjewK])。

模型—视图—控制器(Model-View-Controller，MVC)模式是应用到面向对象编程的Soc原则。
模式的名称来自用来切分软件应用的三个主要部分，即模型部分、视图部分和控制器部分。
MVC 被认为是一种架构模式而不是一种设计模式。架构模式与设计模式之间的区别在于前者比后者的范畴更广。
然而，MVC太重要了，不能仅因为这个原因就跳过不说。

模型是核心的部分，代表着应用的信息本源，包含和管理(业务)逻辑、数据、状态以及应 用的规则。
视图是模型的可视化表现。视图的例子有，计算机图形用户界面、计算机终端的文本 输出、智能手机的应用图形界面、PDF文档、饼图和柱状图等。视图只是展示数据，并不处理数 据。
控制器是模型与视图之间的链接/粘附。
模型与视图之间的所有通信都通过控制器进行(请 参考[GOF95，第14页]、网页[t.cn/RqrjF4G]和网页[t.cn/RPrOUPr])。
'''

'''
模型极为简约，只有一个get_quote()方法，基于索引n从quotes元组中返回对应的名人 名言(字符串)。
注意，n可以小于等于0，因为这种索引方式在Python中是有效的。
'''
quotes = ('A man is not complete until he is married. Then he is finished.',
          'As I said before, I never repeat myself.',
          'Behind a successful man is an exhausted woman.',
          'Black holes really suck...', 'Facts are stubborn things.')

class QuoteModel:

    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError as err:
            value = 'Not found!'
        return value


class QuoteTerminalView:

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see?')


class QuoteTerminalController:

    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError as err:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()
