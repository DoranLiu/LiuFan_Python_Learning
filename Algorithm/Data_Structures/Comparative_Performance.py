'''
Python内置数据结构的性能分析

1.List
2.Dictionary
'''

import random,timeit

#-------------------------===List===-----------------------------
'''
List

# list.index()  O(1)
# list.append() O(1)
# list.pop()    O(1)
# list.pop(i)   O(n)
# list.insert(i,item) O(n)
# list.reverse() O(n)
# list.sort()    O(nlogn)
'''

# 同样是执行1000次创建一个包含1-1000的列表，四种方式使用的时间差距很大.
# 使用append比逐次增加要快很多，另外，使用python的列表产生式比append要快，而第四种方式更加快！
def test1():
   l = []
   for i in range(1000):
      l = l + [i]
def test2():
   l = []
   for i in range(1000):
      l.append(i)
def test3():
   l = [i for i in range(1000)]
def test4():
   l = list(range(1000))

# 生成list的效率比较
t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")
t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")
t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")
t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")
# ('concat ', 1.7890608310699463, 'milliseconds')
# ('append ', 0.13796091079711914, 'milliseconds')
# ('comprehension ', 0.05671119689941406, 'milliseconds')
# ('list range ', 0.014147043228149414, 'milliseconds')

# 删除元素的比较
x1 = list(range(2000000))
pop_zero = timeit.Timer("x1.pop(0)","from __main__ import x1")
print("pop_zero ",pop_zero.timeit(number=1000), "milliseconds")
x2 = list(range(2000000))
pop_end = timeit.Timer("x2.pop()","from __main__ import x2")
print("pop_end ",pop_end.timeit(number=1000), "milliseconds")

# ('pop_zero ', 1.9101738929748535, 'milliseconds')
# ('pop_end ', 0.00023603439331054688, 'milliseconds')

# 插入元素的比较
def test5():
    l = []
    for i in range(1000):
        l.insert(0,i)

def test6():
   l = []
   for i in range(1000):
      l.append(i)

# 生成list的效率比较
t5 = timeit.Timer("test5()", "from __main__ import test5")
print("insert ",t1.timeit(number=1000), "milliseconds")
t6 = timeit.Timer("test6()", "from __main__ import test6")
print("append ",t2.timeit(number=1000), "milliseconds")
# insert  1.830818751011975 milliseconds
# append  0.11050738499034196 milliseconds
#-------------------------===-----------------------------



#-------------------------===Dictionary===-----------------------------
'''
Dictionary

# dict.copy()  O(n)
# dict.get()  O(1)
# dict.set() O(1)
'''

'''
# Dictionary和List的性能比较：
# list基本上随着其元素的数目呈线性增长，而dictionary一直维持在很短很短的时间内。
Dictionary类似Java中的HashMap，内部实现使用了hash函数，所以查找和删除都是常数时间的。
'''
for i in range(10000,1000001,20000):
    t = timeit.Timer("random.randrange(%d) in x"%i,"from __main__ import random,x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j:None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))
'''
10000,     0.090,     0.001
30000,     0.255,     0.001
50000,     0.463,     0.002
70000,     0.665,     0.001
90000,     0.789,     0.001
110000,     1.002,     0.002
130000,     1.336,     0.002
150000,     1.862,     0.002
170000,     1.888,     0.002
190000,     1.915,     0.001
210000,     2.250,     0.001
230000,     2.804,     0.003
'''