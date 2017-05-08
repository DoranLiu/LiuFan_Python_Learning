'''
该模块提供了ConfigParser类，它实现了一种基本配置语言，它提供了类似于Microsoft Windows INI文件中的结构。您可以使用它来编写可由终端用户轻松定制的Python程序。
configparser用于处理特定格式的文件，其本质上是利用开来操作文件。
'''

'''配置文件格式如下：
# 第一种注释方式
; 第二种注释方式'''

'''
[node1]  # 节点
k1 = v1  # key = value
k2 : v2  # key : value
'''

# 实例
# 一个创建 file.conf文件，内容为空，然后进入pythonIDE：

# 为文件添加节点
import configparser
config = configparser.ConfigParser()
config.read('file.conf', encoding='utf-8')

# 添加节点"node1","node2",然后写入文件
config.add_section("node1")
config.add_section("node2")
config.write(open('file.conf', 'w'))

'''# 检查节点是否存在'''
# 如果文件存在则返回"True"，否则就返回"False"
print(config.has_section('node1'))
True
print(config.has_section('node2'))
True
print(config.has_section('node3'))
False

'''删除节点'''
# 如果删除的节点存在则返回"True"，否则返回"False"
config.remove_section("node2")
config.write(open('file.conf', 'w'))
print(config.has_section('node2'))
False

'''设置节点内的键值对'''
# 添加完键值对之后别忘记了写入到文件中
config.set('node1', 'Name', "ansheng")
config.set('node1', 'Blog_URL', "https://blog.ansheng.me")
config.set('node1', 'Hostname', "localhost.localhost")
config.set('node1', 'IP', "127.0.0.1")
config.write(open('file.conf', 'w'))

'''检查节点内的键是否存在'''
# 如果节点的Key存在就返回"True"，否则返回"False"
print(config.has_option('node1', 'Name'))
True
print(config.has_option('node1', 'IP'))
True
print(config.has_option('node1', 'VV'))
False

'''删除节点内的关键'''
# 如果删除的节点存在就返回"True"，否则就返回"False"
config.remove_option('node1', 'IP')
True
config.write(open('file.conf', 'w'))
print(config.has_option('node1', 'IP'))
False

'''获取指定节点下指定键的值'''
# 默认返回的是字符串类型
config.get('node1', 'Name')
'ansheng'
config.get('node1', 'Blog_URL')
'https://blog.ansheng.me'
# 返回的字符串我们可以设置成一下三种数据类型，分别是"int"，"float"，"bool"
# v = config.getint('node1', 'k1')
# v = config.getfloat('node1', 'k1')
# v = config.getboolean('node1', 'k1')

'''获取指定节点下所有的关键'''
# 返回节点下面所有的Key列表
config.options('node1')
['name', 'blog_url', 'hostname']

'''获取指定节点下所有的键值对'''
# 返回一个列表，列表中每个元组就是一个键值对
config.items('node1')
[('name', 'ansheng'), ('blog_url', 'https://blog.ansheng.me'), ('hostname', 'localhost.localhost')]

'''获取所有节点'''
# 获取当前文件中有多少个节点
config.sections()
['node1']