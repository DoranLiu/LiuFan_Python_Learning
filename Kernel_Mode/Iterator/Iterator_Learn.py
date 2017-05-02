'''
如何实现可迭代对象和迭代器对象？
如何使用生成器函数实现可迭代对象？
如何进行反向迭代以及如何实现反向迭代？
如何对迭代器做切片操作？
如何在一个for语句中迭代多个可迭代对象？
'''

'''
如何实现可迭代对象和迭代器对象？

某软件要求从网络抓取各个城市气温信息，并其次显示：
北京： 15 ~ 20
天津： 17 ~ 22
长春： 12 ~ 18
......
如果一次抓取所有城市天气再显示，显示第一个城市气温时，有很高的延时，并且浪费存储空间，我们期望以用时访问的策略，并且把所有城市气温封装到一个对象里，可用for语句进行迭代，如何解决？
'''

# 实现一个迭代器对象Weatherlterator,next方法每次返回一个城市气温，实现一个可迭代对象Weatherlterable,————iter__方法返回一个迭代器对象
import requests
from collections import Iterable, Iterator

# 气温迭代器
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0
    def getWeather(self, city):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s：%s , %s' % (city, data['low'], data['high'])
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

# 可迭代对象
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities
    def __iter__(self):
        return WeatherIterator(self.cities)
for x in WeatherIterable(['北京', '上海', '广州', '深圳']):
    print(x)

'''
如何使用生成器函数实现可迭代对象？

实现一个可迭代对象的类，它能迭代出给定范围内所有素数：
pn = PrimeNumbers(1, 30)
for k in pn:
   print(k)

-将该类的__iter__方法实现生成器函数，每次yield返回一个素数
'''
class PrimeNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True
    def __iter__(self):
        for k in range(self.start, self.stop + 1):
            if self.isPrimeNum(k):
                yield k
for x in PrimeNumbers(1, 20):
    print(x)

'''
如何进行反向迭代以及如何实现反向迭代？

实现一个连续浮点数生成器FloatRange(和rrange类似)，根据给定范围(start, stop)和步进值(step)产生一些列连续浮点数，如迭代FloatRange(3.0,4.0,0.2)可产生序列：
正向：3.0 > 3.2 > 3.4 > 3.6 > 3.8 > 4.0
反向：4.0 > 3.8 > 3.6 > 3.4 > 3.2 > 3.0
'''
class FloatRange:
    def __init__(self, start, stop, step=0.1):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        t = self.start
        while t <= self.stop:
            yield t
            t += self.step
    def __reversed__(self):
        t = self.stop
        while t >= self.start:
            yield t
            t -= self.step
print("正相迭代-----")
for n in FloatRange(1.0, 4.0, 0.5):
    print(n)
print("反迭代-----")
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x)

'''
如何对迭代器做切片操作？

有某个文本文件，我们想都去其中某范围的内容，如100~300行之间的内容，python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式得到一个100~300行文件内容的生成器？

解决方案：
使用标准库中的itertools.islice，它能返回一个迭代器对象切片的生成器
'''
from itertools import islice
f = open('access.log')
# # 前500行
# islice(f, 500)
# # 100行以后的
# islice(f, 100, None)
for line in islice(f,100,300):
    print(line)

# islice每次训话都会消耗之前的迭代对象
l = range(20)
t = iter(l)
for x in islice(t, 5, 10):
    print(x)
print('第二次迭代')
for x in t:
    print(x)

'''
如何在一个for语句中迭代多个可迭代对象？

某班学生期末考试成绩，语文、数学、英语分别存储再3个列表中，同时迭代三个列表，计算每个学生的总分(并行)
某年纪有四个班，某次考试没班英语成绩分别存储在四个列表中，依次迭代每个列表，统计全学年成绩高于90分人数(串行)
'''

# 解决方案：
# 并行：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
from random import randint
# 申城语文成绩，# 40人，分数再60-100之间
chinese = [randint(60, 100) for _ in range(40)]
math = [randint(60, 100) for _ in range(40)]  # 数学
english = [randint(60, 100) for _ in range(40)]  # 英语
total = []
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)
print(total)

# 串行：使用标准库中的itertools.chain，它能将多个可迭代对象连接
from random import randint
from itertools import chain
# 生成四个班的随机成绩
e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(42)]
e3 = [randint(60, 100) for _ in range(45)]
e4 = [randint(60, 100) for _ in range(50)]
# 默认人数=1
count = 0
for s in chain(e1, e2, e3, e4):
    # 如果当前分数大于90，就让count+1
    if s > 90:
        count += 1
print(count)

