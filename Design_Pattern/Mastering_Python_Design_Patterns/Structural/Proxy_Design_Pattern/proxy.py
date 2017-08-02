# coding: utf-8
'''
在某些应用中，我们想要在访问某个对象之前执行一个或多个重要的操作，例如，访问敏感信息——在允许用户访问敏感信息之前，我们希望确保用户具备足够的权限。
操作系统中也存在类似的情况，用户必须具有管理员权限才能在系统中安装新程序。

上面提到的重要操作不一定与安全问题相关。延迟初始化(请参考网页[t.cn/Ryf47bV]) 是另一个案例:我们想要把一个计算成本较高的对象的创建过程延迟到用户首次真正使用它时才进行。
这类操作通常使用代理设计模式(Proxy design pattern)来实现。该模式因使用代理(又名 替代，surrogate)对象在访问实际对象之前执行重要操作而得其名。

以下是四种不同的知名代理 类型(请参考[GOF95，第234页]和网页[t.cn/RqrYEn9])。
 远程代理:实际存在于不同地址空间(例如，某个网络服务器)的对象在本地的代理者。
 虚拟代理:用于懒初始化，将一个大计算量对象的创建延迟到真正需要的时候进行。
 保护/防护代理:控制对敏感对象的访问。
 智能(引用)代理:在对象被访问时执行额外的动作。此类代理的例子包括引用计数和线程安全检查。

应用场景：
 在使用私有网络或云搭建一个分布式系统时。在分布式系统中，一些对象存在于本地内 存中，一些对象存在于远程计算机的内存中。如果我们不想本地代码关心两者之间的区别，那么可以创建一个远程代理来隐藏/封装，使得应用的分布式性质透明化。
 因过早创建计算成本较高的对象导致应用遭受性能问题之时。使用虚拟代理引入懒初始 化，仅在真正需要对象之时才创建，能够明显提高性能。
 用于检查一个用户是否有足够权限来访问某个信息片段。如果应用要处理敏感信息(例 如，医疗数据)，我们会希望确保用户在被准许之后才能访问/修改数据。一个保护/防护 代理可以处理所有安全相关的行为。
 应用(或库、工具集、框架等)使用多线程，而我们希望把线程安全的重任从客户端代码转移到应用。这种情况下，可以创建一个智能代理，对客户端隐藏线程安全的复杂性。
 对象关系映射(Object-Relational Mapping，ORM)API也是一个如何使用远程代理的例子。包括Django在内的许多流行Web框架使用一个ORM来提供类OOP的关系型数据库访问。 ORM是关系型数据库的代理，数据库可以部署在任意地方，本地或远程服务器都可以。

'''

# SensitiveInfo类包含我们希望保护的信息。
# users变量是已有用户的列表。read()方法输出用户列表，这一操作不要求特殊权限。
# add()方法将一个新用户添加到列表中，这一操作要求客户端提供一个特殊的密码。
class SensitiveInfo:

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))

# Info类是SensitiveInfo的一个保护代理。
# secret变量值是客户端代码在添加新用户时被要求告知/提供的密码。
# 注意，这只是一个例子。现实中，永远不要执行以下操作。
#  在源代码中存储密码
#  以明文形式存储密码
#  使用一种弱(例如，MD5)或自定义加密形式

class Info:

    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))

if __name__ == '__main__':
    main()
