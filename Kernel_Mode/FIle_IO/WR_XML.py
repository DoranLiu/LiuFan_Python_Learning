'可以使用标准库中的xml.etree.ElementTree，其中的parse函数可以解析XML文档'

xml_string = """<?xml version="1.0" encoding="utf-8" ?>
<data>
    <country name="Liechtenstein">
        <rank update="yes">2</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank update="yes">5</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank update="yes">69</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

# 导入parse
from xml.etree.ElementTree import parse
# f = open('a.xml')
f = xml_string
# 获得ElementTree对象
et = parse(f)
# 获取根节点，也就是data
root = et.getroot()
# 查看标签
print(root.tag)
# 属性
print(root.attrib)
# 文本
print(root.text.strip())

# 获得一个节点的子元素，然后在获取每个子元素的属性
for child in root: print(child.get('name'))

# 根据标签寻找子元素，每次之寻找第一个
print(root.find('country'))
# 寻找所有
print(root.findall('country'))
# 获得一个生成器对象
print(root.iterfind('country'))

for e in root.iterfind('country'): print(e.get('name'))

# 获取所有的元素节点
print(list(root.iter()))
# 寻找标签为rank的子节点
print(list(root.iter('rank')))

# 匹配country下的所有子节点
root.findall('country/*')

# 找到所有节点的rank
root.findall('.//rank')

# 找到rank的父对象
root.findall('.//rank/..')

# 查找country包含name属性的
root.findall('country[@name]')

# 查找属性等于特定值的元素
root.findall('country[@name="Singapore"]')

# 查找必须包含某一个子元素
root.findall('country[rank]')

# 查找子元素等于指定的值
root.findall('country[rank="5"]')

# 根据位置查找，从1开始
root.findall('country')

# 根据位置查找
root.findall('country[1]')

# 倒数第一个
root.findall('country[last()]')

# 倒数第二个
root.findall('country[last()-1]')


'''
如何构建xml文档？
某些时候，我们需要将其他格式数据转换为xml，例如下面的字符串如何转换为XML？
'''
import csv
from xml.etree.ElementTree import Element, ElementTree
def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level
def csvToXML(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                eRow.append(e)
    pretty(root)
    return ElementTree(root)
et = csvToXML('pingan.csv')
et.write('pingan.xml')
