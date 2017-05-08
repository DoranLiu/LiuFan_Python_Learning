'''
如何让对象支持上下文管理?

实际案例
我们实现了一个Telnet客户端的类TelnetClient，
调用实例的start()方法启动客户端与服务器交互，
交互完毕后需调用cleanup()方法，关闭已链接的socket，
以及将操作历史记录写入文件并关闭.

能否让TelnetClient的实例实现上下文管理协议，从而替代手工调用cleanup()方法

解决方案
实现上下文管理协议，需定义实例的__enter__，__exit__方法，他们分别在with开始和结束时被调用。
'''

from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque
class TelnetClient:
    def __init__(self, addr, port=23):
        self.addr = addr
        self.port = port
        self.tn = None
    def start(self):
        # user
        t = self.tn.read_until('login: ')
        stdout.write(t)
        user = stdin.readline()
        self.tn.write(user)
        # password
        t = self.tn.read_until('Password: ')
        if t.startswith(user[:-1]): t = t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())
        t = self.tn.read_until('$ ')
        stdout.write(t)
        while True:
            uinput = stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t = self.tn.read_until('$ ')
            stdout.write(t[len(uinput) + 1:])
    def __enter__(self):
        self.tn = Telnet(self.addr, self.port)  # 创建链接
        self.history = deque()  # 创建历史记录队列
        return self  # 返回当前的实例
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type: 异常类型
        :param exc_val: 异常值
        :param exc_tb: 跟踪的栈
        :return:
        """
        self.tn.close()  # 关闭链接
        self.tn = None
        with open(self.addr + '_history.txt', 'w') as f:
            """ 把历史记录写入文件中 """
            f.writelines(self.history)
            # return True  # 如果返回True，即使出错也会往下继续执行
with TelnetClient('127.0.0.1') as client:
    client.start()