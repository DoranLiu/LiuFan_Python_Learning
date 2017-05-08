2.1.  Compile
Python通过re模块提供对正则表达式的支持。
使用re的一般步骤是：
Step1：先将正则表达式的字符串形式编译为Pattern实例。
Step2：然后使用Pattern实例处理文本并获得匹配结果（一个Match实例）。
Step3：最后使用Match实例获得信息，进行其他的操作。

我们新建一个re01.py来试验一下re的应用：
```
1. # -*- coding: utf-8 -*-
2. #一个简单的re实例，匹配字符串中的hello字符串
3.
4. #导入re模块
5. import re
6.
7. # 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
8. pattern = re.compile(r'hello')
9.
10. # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
11. match1 = pattern.match('hello world!')
12. match2 = pattern.match('helloo world!')
13. match3 = pattern.match('helllo world!')
14.
15. #如果match1匹配成功
16. if match1:
17.     # 使用Match获得分组信息
18.     print match1.group()
19. else:
20.     print 'match1匹配失败！'
21.
22.
23. #如果match2匹配成功
24. if match2:
25.     # 使用Match获得分组信息
26.     print match2.group()
27. else:
28.     print 'match2匹配失败！'
29.
30.
31. #如果match3匹配成功
32. if match3:
33.     # 使用Match获得分组信息
34.     print match3.group()
35. else:
36.     print 'match3匹配失败！'
可以看到控制台输出了匹配的三个结果：
```

下面来具体看看代码中的关键方法。
★ re.compile(strPattern[, flag]):
这个方法是Pattern类的工厂方法，用于将字符串形式的正则表达式编译为Pattern对象。
第二个参数flag是匹配模式，取值可以使用按位或运算符'|'表示同时生效，比如re.I | re.M。
另外，你也可以在regex字符串中指定模式，
比如re.compile('pattern', re.I | re.M)与re.compile('(?im)pattern')是等价的。

可选值有：
*     re.I(全拼：IGNORECASE): 忽略大小写（括号内是完整写法，下同）
*    re.M(全拼：MULTILINE): 多行模式，改变'^'和'$'的行为（参见上图）
*     re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
*     re.L(全拼：LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
*     re.U(全拼：UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
*     re.X(全拼：VERBOSE): 详细模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。

以下两个正则表达式是等价的：
```
1. # -*- coding: utf-8 -*-
2. #两个等价的re匹配,匹配一个小数
3. import re
4.
5. a = re.compile(r"""\d +  # the integral part
6.                    \.    # the decimal point
7.                    \d *  # some fractional digits""", re.X)
8.
9. b = re.compile(r"\d+\.\d*")
10.
11. match11 = a.match('3.1415')
12. match12 = a.match('33')
13. match21 = b.match('3.1415')
14. match22 = b.match('33')
15.
16. if match11:
17.     # 使用Match获得分组信息
18.     print match11.group()
19. else:
20.     print u'match11不是小数'
21.
22. if match12:
23.     # 使用Match获得分组信息
24.     print match12.group()
25. else:
26.     print u'match12不是小数'
27.
28. if match21:
29.     # 使用Match获得分组信息
30.     print match21.group()
31. else:
32.     print u'match21不是小数'
33.
34. if match22:
35.     # 使用Match获得分组信息
36.     print match22.group()
37. else:
38.     print u'match22不是小数'
```
re提供了众多模块方法用于完成正则表达式的功能。

这些方法可以使用Pattern实例的相应方法替代，唯一的好处是少写一行re.compile()代码，
但同时也无法复用编译后的Pattern对象。
这些方法将在Pattern类的实例方法部分一起介绍。

```
1. # -*- coding: utf-8 -*-
2. #一个简单的re实例，匹配字符串中的hello字符串
3. import re
4.
5. m = re.match(r'hello', 'hello world!')
6. print m.group()
```
re模块还提供了一个方法escape(string)，用于将string中的正则表达式元字符如*/+/?等之前加上转义符再返回
