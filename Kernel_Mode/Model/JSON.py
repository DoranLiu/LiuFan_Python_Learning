'''
JSON通常用于在Web客户端和服务器数据交换，即把字符串类型的数据转换成Python基本数据类型或者将Python基本数据类型转换成字符串类型。

常用方法

方法	说明
json.loads(obj)	将字符串序列化成Python的基本数据类型，注意单引号与双引号
json.dumps(obj)	将Python的基本数据类型序列化成字符串
json.load(obj)	读取文件中的字符串，序列化成Python的基本数据类型
json.dump(obj)	将Python的基本数据类型序列化成字符串并写入到文件中
'''

'''
实例
将字符串序列化成字典
创建一个字符串变量dict_str
'''
dict_str = '{"k1":"v1","k2":"v2"}'
# 数据类型为str
type(dict_str)
# <class 'str'>
# 将字符串变量dict_str序列化成字典格式

import json
dict_json = json.loads(dict_str)

# 查看数据类型并输出内容
type(dict_json)
# 数据类型被序列化成字典格式了
# <class 'dict'>
dict_json
{'k1': 'v1', 'k2': 'v2'}
# 将一个列表类型的变量序列化成字符串类型
# 创建一个列表json_li

json_li = [11,22,33,44]
# 数据类型为list
type(json_li)
# <class 'list'>
# 将字符串类型转换为Python的基本数据类型
json_str = json.dumps(json_li)

# 查看数据类型

# 为str
type(json_str)
# <class 'str'>
json_str
'[11, 22, 33, 44]'
# 把字典当作字符串存入db文件当中
# 创建一个字典的数据类型
dic = {"k1":123,"k2":456}
# 输出类型及内容
print(type(dic),dic)
# (<type 'dict'>, {'k2': 456, 'k1': 123})
# 导入json模块
import json
# 将dic转换为字符串并且写入到当前目录下面的db文件内，如果没有该文件则创建
json.dump(dic,open("db","w"))
# 导入os模块查看
import os
# 查看当前目录下面的文件
os.system("ls -l")
# total 8
# -rw-r--r-- 1 root root 22 May 20 23:54 db
# 0
# 查看文件db的内容那个，最后面那个0是代表命令执行成功
os.system("cat db")
# {"k2": 456, "k1": 123}
# 0
# 读取文件内容，把读取出来的字符串转换成Python的基本数据类型
# 读取当前目录下面的db文件，把内容转换为Python的基本数据类型并赋值给result
result = json.load(open("db","r"))
# 查看对象result的数据类型及内容
print(type(result),result)
# (<type 'dict'>, {u'k2': 456, u'k1': 123})