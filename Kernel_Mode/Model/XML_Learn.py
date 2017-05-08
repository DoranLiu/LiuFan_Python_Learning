'''
https://blog.ansheng.me/article/python-standard-library-xml/

XML的一些重要特性

以标签一个<字符开头和结尾，例如实例中的饲料，标题，副标题，作者。
忽略空格
通常一个开始标签跟一段其他的内容，然后是最后相匹配的结束标签，例如大好时光！
标签之间是可以存在多级嵌套的
可选属性（属性）可以出现在开始标签里
标签中可以包含值（值）
如果命名一个为thing的标签内没有内容或者子标签，那么它可以用在右尖括号的前面添加斜杠的简单标签所表示，例如代替开始和结束都存在的标签。
存放数据的位置可以是任意的 - 属性，值或者子标签。
XML通常用于数据传送和消息，它们存在于一些子格式，如RSS和Atom，例如：https : //blog.ansheng.me/atom.xml

在Python的中解析XML最简单的方法是使用ElementTree。

模块	说明
xml.etree.ElementTree	ElementTree API，一个简单而轻量级的XML处理器
创建XML文件

导入ElementTree的方法，起一个别名为ET

>>> from xml.etree import ElementTree as ET
创建顶级标签

>>> level_1 = ET.Element("famliy")
创建二级标签，标签名名，ATTRIB标签属性

>>> level_2 = ET.SubElement(level_1, "name", attrib={"enrolled":"yes"})
创建三级标签

>>> level_3 = ET.SubElement(level_2, "age", attrib={"checked":"no"})
生成文档

>>> tree = ET.ElementTree(level_1)
写入文件中

>>> tree.write('oooo.xml',encoding='utf-8', short_empty_elements=False)
导入口模块，用OS模块中的系统方法执行外壳命令查看刚才创建的oooo.xml文件

>>> import os
>>> os.system("cat oooo.xml")
# 生成出来的文档是没有换行的
<famliy><name enrolled="yes"><age checked="no"></age></name></famliy>0
把刚才生成的文件下载到本地，然后用浏览器打开就可以看到分级层次了。

XML模块-01

创建一个有换行的XML文件

代码

from xml.etree import ElementTree as ET
from xml.dom import minidom
root = ET.Element('level1',{"age":"1"})
son = ET.SubElement(root,"level2",{"age":"2"})
ET.SubElement(son, "level3", {"age":"3"})
# tree = ET.ElementTree(root)
# tree.write("abc.xml", encoding="utf-8",xml_declaration=True,short_empty_elements=False)
def prettify(root):
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")
new_str = prettify(root)
f = open("new_out.xml", "w")
f.write(new_str)
f.close()
生成的XML文件

<?xml version="1.0" ?>
<level1 age="1">
    <level2 age="2">
        <level3 age="3"/>
    </level2>
</level1>
解析XML

first.xml文件内容为：

<data>
    <country name="Liechtenstein">
        <rank updated="yes">2</rank>
        <year age="19">2025</year>
        <gdppc>141100</gdppc>
        <neighbor direction="E" name="Austria" />
        <neighbor direction="W" name="Switzerland" />
    </country>
    <country name="Singapore">
        <rank updated="yes">5</rank>
        <year age="19">2028</year>
        <gdppc>59900</gdppc>
        <neighbor direction="N" name="Malaysia" />
    </country>
    <country name="Panama">
        <rank updated="yes">69</rank>
        <year age="19">2028</year>
        <gdppc>13600</gdppc>
        <neighbor direction="W" name="Costa Rica" />
        <neighbor direction="E" name="Colombia" />
    </country>
</data>
first.xml在文件/root目录下

利用ElementTree.XML将字符串解析成XML对象

>>> from xml.etree import ElementTree as ET
# 打开文件，读取XML内容，将字符串解析成xml特殊对象，root代指xml文件的根节点
>>> root = ET.XML(open('first.xml', 'r').read())
>>> root.tag
'data'
>>> for node in root:
...  print(node.tag, node.attrib)
...
('country', {'name': 'Liechtenstein'})
('country', {'name': 'Singapore'})
('country', {'name': 'Panama'})
>>> print(node.find('rank').text)
69
利用ElementTree.parse将文件直接解析成XML对象

>>> from xml.etree import ElementTree as ET
# 直接解析xml文件
>>> tree = ET.parse("first.xml")
# 获取xml文件的根节点
>>> root = tree.getroot()
>>> root.tag
'data'
遍历XML中指定的节点

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> for node in root.iter('year'):
        # 输出node的tag和内容
...     print(node.tag, node.text)
...
year 2025
year 2028
year 2028
增，删，改XML

为节点添加属性

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> for node in root.iter("year"):
        # 查看原来的属性
...     print(node.attrib)
...
{}
{}
{}
>>> for node in root.iter("year"):
       # 添加属性
...    node.set("OS","Linux")
...
>>> for node in root.iter("year"):
        # 查看添加的属性
...     print(node.attrib)
...
{'OS': 'Linux'}
{'OS': 'Linux'}
{'OS': 'Linux'}
# 把内容写入文件
>>> tree.write("first.xml")
删除节点属性

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> for node in root.iter("year"):
        # 删除节点的OS属性
...     del node.attrib['OS']
...
# 写入到文件当中
>>> tree.write("first.xml")
查看属性

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> for node in root.iter("year"):
...  print(node.attrib)
...
# 节点内容为空
{}
{}
{}
修改节点内容

修改year内的数字自加1

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> for node in root.iter("year"):
        # 输出原来year的内容
...     print(node.text)
        # 原来的值自加+
...     new_year = int(node.text) + 1
...     node.text = str(new_year)
...
2025
2028
2028
# 写入文件中
>>> tree.write("first.xml")
>>> for node in root.iter("year"):
        # 输出写入文件之后year的内容
...     print(node.text)
...
2026
2029
2029
对节点操作的方法

获取节点的方法

>>> from xml.etree import ElementTree as ET
>>> tree = ET.parse("first.xml")
>>> root = tree.getroot()
>>> print(dir(root))
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'extend', 'find', 'findall', 'findtext', 'get', 'getchildren', 'getiterator', 'insert', 'items', 'iter', 'iterfind', 'itertext', 'keys', 'makeelement', 'remove', 'set']
方法有这么多，那么我们常用的也就是下面的几个

方法名	说明
标签	获取标签标签名
ATTRIB	获取节点的属性
找	获取节点的内容
ITER	进行迭代
组	设置属性
得到	获取属性
实例

判断QQ是否在线

腾讯提供了能够查看QQ号码是否在线的API，Y=在线; N=离线; E= QQ号码错误; A=商业用户验证失败; V=免费用户超过数量

>>> import requests
>>> from xml.etree import ElementTree as ET
>>> r = requests.get("http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=6087414")
>>> result = r.text
>>> from xml.etree import ElementTree as ET
>>> node = ET.XML(result)
>>> if node.text == "Y":
...    print("在线")
... else:
...    print("离线")
...
在线
获取列车起止时间

代码

r = requests.get("http://www.webxml.com.cn/WebServices/TrainTimeWebService.asmx/getDetailInfoByTrainCode?TrainCode=K234&UserID=")
result = r.text
root = ET.XML(result)
for node in root.iter('TrainDetailInfo'):
    print(node.find('TrainStation').text,node.find('ArriveTime').text,node.find("StartTime").text)
执行结果

C:\Python35\python.exe F:/Python_code/sublime/Week5/Day01/xml_mod.py
上海（车次：K234\K235） None 11:12:00
# 地点 停止    启动
昆山 11:45:00 11:48:00
苏州 12:12:00 12:16:00
无锡 12:44:00 12:55:00
常州 13:22:00 13:26:00
镇江 14:13:00 14:16:00
南京 15:04:00 15:16:00
蚌埠 17:27:00 17:50:00
徐州 19:38:00 19:58:00
商丘 22:12:00 22:17:00
开封 23:49:00 23:53:00
郑州 00:37:00 01:14:00
新乡 02:20:00 02:22:00
鹤壁 03:01:00 03:03:00
安阳 03:33:00 03:36:00
邯郸 04:11:00 04:16:00
邢台 04:47:00 04:51:00
石家庄 06:05:00 None
Process finished with exit code 0
'''