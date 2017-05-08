###字符说明：

####1.非打印字符
- \cx	匹配由x指明的控制字符。例如， \cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。否则，将 c 视为一个原义的 'c' 字符。
- \f	匹配一个换页符。等价于 \x0c 和 \cL。
- \n	匹配一个换行符。等价于 \x0a 和 \cJ。
- \r	匹配一个回车符。等价于 \x0d 和 \cM。
- \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
- \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
- \t	匹配一个制表符。等价于 \x09 和 \cI。
- \v	匹配一个垂直制表符。等价于 \x0b 和 \cK。

####2.特殊字符
- $	匹配输入字符串的结尾位置。如果设置了 RegExp 对象的 Multiline 属性，则 $ 也匹配 '\n' 或 '\r'。要匹配 $ 字符本身，请使用 \$。
- ( )	标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用。要匹配这些字符，请使用 \( 和 \)。
- *	匹配前面的子表达式零次或多次。要匹配 * 字符，请使用 \*。
- +	匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
- .	匹配除换行符 \n 之外的任何单字符。要匹配 . ，请使用 \. 。
- [	标记一个中括号表达式的开始。要匹配 [，请使用 \[。
- ?	匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 字符，请使用 \?。
- \	将下一个字符标记为或特殊字符、或原义字符、或向后引用、或八进制转义符。例如， 'n' 匹配字符 'n'。'\n' 匹配换行符。序列 '\\' 匹配 "\"，而 '\(' 则匹配 "("。
- ^	匹配输入字符串的开始位置，除非在方括号表达式中使用，此时它表示不接受该字符集合。要匹配 ^ 字符本身，请使用 \^。
- {	标记限定符表达式的开始。要匹配 {，请使用 \{。
- |	指明两项之间的一个选择。要匹配 |，请使用 \|。

####3.限定符
- *	匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
- +	匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
- ?	匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 中的"do" 。? 等价于 {0,1}。
- {n}	n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
- {n,}	n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
- {n,m}	m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。

####4.定位符
- ^	匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配。
- $	匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配。
- \b	匹配一个字边界，即字与空格间的位置。
- \B	非字边界匹配。


贪婪模式，总是尝试匹配尽可能多的字符;非贪婪模式则相反，总是尝试匹配尽可能少的字符。
Python里的原生字符串很好地解决了这个问题，这个例子中的正则表达式可以使用r"\\"表示。
同样，匹配一个数字的"\\d"可以写成r"\d"。

二、 介绍re模块

• match(): 匹配字符串开始位置。
• search(): 扫描字符串，找到第 个位置。 
• findall(): 找到全部匹配，以列表返回。
• finditer(): 找到全部匹配，以迭代器返回。

match 和search 仅匹配一次，匹配不到返回None。

- 编译标志
• s: 单行。"." 匹配包括换 符在内的所有字符。
• i: 忽略大小写。
• L: 让 "\w" 能匹配当地字符，貌似对中  持不好。 
• m:多行。
• x: 忽略多余的空 字符，让表达式更易阅读。 
• u: Unicode。



2.3. Pattern

Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。

Pattern不能直接实例化，必须使用re.compile()进行构造，也就是re.compile()返回的对象。

Pattern提供了几个可读属性用于获取表达式的相关信息：

1. pattern: 编译时用的表达式字符串。
2. flags: 编译时用的匹配模式。数字形式。
3. groups: 表达式中分组的数量。 
4. groupindex: 以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。
可以用下面这个例子查看pattern的属性：


1. # -*- coding: utf-8 -*-  
2. #一个简单的pattern实例  
3.   
4. import re  
5. p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)  
6.    
7. print "p.pattern:", p.pattern  
8. print "p.flags:", p.flags  
9. print "p.groups:", p.groups  
10. print "p.groupindex:", p.groupindex  
11.    
12. ### output ###  
13. # p.pattern: (\w+) (\w+)(?P<sign>.*)  
14. # p.flags: 16  
15. # p.groups: 3  
16. # p.groupindex: {'sign': 3}  
下面重点介绍一下pattern的实例方法及其使用。









2.search
search(string[, pos[, endpos]]) | re.search(pattern, string[, flags]): 
这个方法用于查找字符串中可以匹配成功的子串。

从string的pos下标处起尝试匹配pattern，

如果pattern结束时仍可匹配，则返回一个Match对象；

若无法匹配，则将pos加1后重新尝试匹配；

直到pos=endpos时仍无法匹配则返回None。

pos和endpos的默认值分别为0和len(string))；

re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。

那么它和match有什么区别呢？

match()函数只检测re是不是在string的开始位置匹配，

search()会扫描整个string查找匹配，



match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
例如：
print(re.match(‘super’, ‘superstition’).span())

会返回(0, 5)

print(re.match(‘super’, ‘insuperable’))

则返回None

search()会扫描整个字符串并返回第一个成功的匹配
例如：

print(re.search(‘super’, ‘superstition’).span())

返回(0, 5)
print(re.search(‘super’, ‘insuperable’).span())

返回(2, 7)

看一个search的实例：



1. # -*- coding: utf-8 -*-  
2. #一个简单的search实例  
3.   
4. import re  
5.    
6. # 将正则表达式编译成Pattern对象  
7. pattern = re.compile(r'world')  
8.    
9. # 使用search()查找匹配的子串，不存在能匹配的子串时将返回None  
10. # 这个例子中使用match()无法成功匹配  
11. match = pattern.search('hello world!')  
12.    
13. if match:  
14.     # 使用Match获得分组信息  
15.     print match.group()  
16.    
17. ### 输出 ###  
18. # world  






3.split

split(string[, maxsplit]) | re.split(pattern, string[, maxsplit]):
按照能够匹配的子串将string分割后返回列表。

maxsplit用于指定最大分割次数，不指定将全部分割。



1. import re  
2.    
3. p = re.compile(r'\d+')  
4. print p.split('one1two2three3four4')  
5.    
6. ### output ###  
7. # ['one', 'two', 'three', 'four', '']  





4.findall

findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags]):
搜索string，以列表形式返回全部能匹配的子串。

1. import re  
2.    
3. p = re.compile(r'\d+')  
4. print p.findall('one1two2three3four4')  
5.    
6. ### output ###  
7. # ['1', '2', '3', '4']  




5.finditer

finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags]):
搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。



1. import re  
2.    
3. p = re.compile(r'\d+')  
4. for m in p.finditer('one1two2three3four4'):  
5.     print m.group(),  
6.    
7. ### output ###  
8. # 1 2 3 4  



6.sub

sub(repl, string[, count]) | re.sub(pattern, repl, string[, count]):
使用repl替换string中每一个匹配的子串后返回替换后的字符串。 
当repl是一个字符串时，可以使用\id或\g<id>、\g<name>引用分组，但不能使用编号0。 
当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 
count用于指定最多替换次数，不指定时全部替换。


1. import re  
2.    
3. p = re.compile(r'(\w+) (\w+)')  
4. s = 'i say, hello world!'  
5.    
6. print p.sub(r'\2 \1', s)  
7.    
8. def func(m):  
9.     return m.group(1).title() + ' ' + m.group(2).title()  
10.    
11. print p.sub(func, s)  
12.    
13. ### output ###  
14. # say i, world hello!  
15. # I Say, Hello World!  

7.subn
subn(repl, string[, count]) |re.sub(pattern, repl, string[, count]):
返回 (sub(repl, string[, count]), 替换次数)。



1. import re  
2.    
3. p = re.compile(r'(\w+) (\w+)')  
4. s = 'i say, hello world!'  
5.    
6. print p.subn(r'\2 \1', s)  
7.    
8. def func(m):  
9.     return m.group(1).title() + ' ' + m.group(2).title()  
10.    
11. print p.subn(func, s)  
12.    
13. ### output ###  
14. # ('say i, world hello!', 2)  
15. # ('I Say, Hello World!', 2)