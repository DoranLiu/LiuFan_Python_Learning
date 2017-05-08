# 标准库 itertools 模块是不应该忽视的宝藏。
import itertools

'''
chain
连接多个迭代器。
'''
it_chain = itertools.chain(range(3), "abc")
# [0, 1, 2, 'a', 'b', 'c']

'''
combinations
返回指定 度的元素顺序组合序列。
'''
it_combinations = itertools.combinations("abcd", 2)
# [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

it_combinations2 =itertools.combinations(range(4), 2)
# [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

'''
combinations_with_replacement
会额外返回同 元素的组合。
'''
it_combinations_with_replacement = itertools.combinations_with_replacement("abcd", 2)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'b'), ('b', 'c'), ('b', 'd'),
# ('c', 'c'), ('c', 'd'), ('d', 'd')]

'''
compress
按条件表过滤迭代器元素。
条件列表可以是任何布尔列表
'''
it_compress = itertools.compress("abcde", [1, 0, 1, 1, 0])
# ['a', 'c', 'd']

'''
count
从起点开始，"无限" 循环下去。
'''
for x in itertools.count(10, step = 2):
    print (x)
    if x > 17: break
# 10 12 14 16 18

'''
cycle
迭代结束，再从头来过。
'''
for i, x in enumerate(itertools.cycle("abc")):
    print (x)
    if i > 7: break
# a b c a b c a b c

'''
dropwhile
跳过头部符合条件的元素。
takewhile 则仅保留头部符合条件的元素。
'''
it_dropwhile = itertools.dropwhile(lambda i: i < 4, [2, 1, 4, 1, 3])
# [4, 1, 3]

it_takewhile = itertools.takewhile(lambda i: i < 4, [2, 1, 4, 1, 3])
 # [2, 1]

'''
groupby
将连续出现的相同元素进 分组。
'''
[list(k) for k, g in itertools.groupby('AAAABBBCCDAABBCCDD')]
# [['A'], ['B'], ['C'], ['D'], ['A'], ['B'], ['C'], ['D']]

[list(g) for k, g in itertools.groupby('AAAABBBCCDAABBCCDD')]
# [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D'], ['A', 'A'], ['B', 'B'], ['C','C'], ['D', 'D']]

'''
ifilter
与内置函数 filter() 类似，仅保留符合条件的元素。
ifilterfalse 正好相反，保留不符合条件的元素。
'''
it_ifilter = itertools.ifilter(lambda x: x % 2, range(10))
# [1, 3, 5, 7, 9]

it_ifilterfalse = itertools.ifilterfalse(lambda x: x % 2, range(10))
# [0, 2, 4, 6, 8]

'''
imap
与内置函数 map() 类似。
'''
it_imap = itertools.imap(lambda x, y: x + y, (2,3,10), (5,2,3))
# [7, 5, 13]

'''
islice
以切片的形式从迭代器获取元素。
'''
it_islice1 = itertools.islice(range(10), 3)
# [0, 1, 2]

it_islice2 = itertools.islice(range(10), 3, 5)
 # [3, 4]
it_islice3 = itertools.islice(range(10), 3, 9, 2)
# [3, 5, 7]

'''
izip
与内置函数 zip() 类似，多余元素会被抛弃。
要保留多余元素可以用izip_longest，它提供了一个补缺参数。
'''
it_izip = itertools.izip("abc", [1, 2])
# [('a', 1), ('b', 2)]
it_izip_longest = itertools.izip_longest("abc", [1, 2], fillvalue = 0)
# [('a', 1), ('b', 2), ('c', 0)]

'''
permutations
与 combinations 顺序组合不同，permutations让每个元素都从头组合一遍。
'''
it_permutations = itertools.permutations("abc", 2)
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

it_combinations_f = itertools.combinations("abc", 2)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

'''
product
让每个元素都和后 的迭代器完整组合一遍。
'''
it_product = itertools.product("abc", [0, 1])
# [('a', 0), ('a', 1), ('b', 0), ('b', 1), ('c', 0), ('c', 1)]

'''
repeat
将一个对象重复n次。
'''
it_repeat = itertools.repeat("a", 3)
# ['a', 'a', 'a']

'''
starmap
按顺序处理每组元素。
'''
it_starmap = itertools.starmap(lambda x, y: x + y, [(1, 2), (10, 20)])
# [3, 30]

'''
tee
复制迭代器。
'''
for it in itertools.tee(range(5), 3):
    print (list(it))
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
