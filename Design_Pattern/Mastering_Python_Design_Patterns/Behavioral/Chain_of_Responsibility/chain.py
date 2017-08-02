'''
责任链(Chain of Responsibility)
节点对一个请求的反应方式是实现的细节。
然而，我们可以使用广播计算机网络的类比来理解责任链模式是什么。
责任链(Chain of Responsibility)模式用于让多个对象来处理单个请求时，或者用于预先不知道应该由哪个对象(来自某个对象链)来处理某个特定请求时。
其原则如下所示:
(1) 存在一个对象链(链表、树或任何其他便捷的数据结构)。
(2) 我们一开始将请求发送给链中的第一个对象。
(3) 对象决定其是否要处理该请求。
(4) 对象将请求转发给下一个对象。
(5) 重复该过程，直到到达链尾。

另一个责任链可以派上用场的场景是，在我们知道可能会有多个对象都需要对同一个请求进 行处理之时。这在基于事件的编程中是常有的事情。单个事件，比如一次鼠标左击，可被多个事 件监听者捕获。
不过应该注意，如果所有请求都能被单个处理程序处理，责任链就没那么有用了，除非确实不知道会是哪个程序处理请求。
这一模式的价值在于解耦。客户端与所有处理程序(一个处理程 序与所有其他处理程序之间也是如此)之间不再是多对多关系，客户端仅需要知道如何与链的起 始节点(标头)进行通信。
'''

# Event类描述一个事件。
class Event:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

# Widget类是应用的核心类。
class Widget:

    def __init__(self, parent=None):
        self.parent = parent
    # handle()方法使用动态分发，通过hasattr()和getattr()决定一个特定请求(event) 应该由谁来处理。
    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


'''
MainWindow、MsgText和SendDialog是具有不同行为的控件。我们并不期望这三个控件 都能处理相同的事件，即使它们能处理相同事件，表现出来也可能是不同的。
'''
class MainWindow(Widget):

    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):

    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):

    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == '__main__':
    main()
