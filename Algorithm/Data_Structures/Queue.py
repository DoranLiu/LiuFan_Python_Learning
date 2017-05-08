'''
Queue:
队列：FIFO结构，先进先出
并发中使用较多，可以安全的将对象从一个任务传给另一个任务。

应用：
队列一般用于解决需要优先队列的问题或者进行广度优先搜索的问题，也很简单。

实现：
Queue 和 Stack 在 Python 中都是有 list ,[] 实现的。
在python 中list是一个dynamic array, 可以通过append在list的尾部添加元素， 通过pop()在list的尾部弹出元素实现Stack的FILO， 如果是pop(0)则弹出头部的元素实现Queue的FIFO。

'''

# 一、直接list实现
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
print(queue[0]) # return 2 examine the first element”


# 二、class实现：
class Queue:
   def __init__(self):
      self.items = []

   def is_empty(self):
      return self.items == []

   def enqueue(self, item):
      self.items.append(item)

   def dequeue(self):
      return self.items.pop(0)

   def size(self):
      return len(self.items)


q = Queue()
q.enqueue('hello')
q.enqueue('dog')
print(q.items)
q.enqueue(3)
q.dequeue()
print(q.items)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=Priority_Queue-优先队列-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''


# Priority Queue - 优先队列
# 未写完
'''
# 应用程序常常需要处理带有优先级的业务，优先级最高的业务首先得到服务。因此优先队列这种数据结构应运而生。
优先队列中的每个元素都有各自的优先级，优先级最高的元素最先得到服务；优先级相同的元素按照其在优先队列中的顺序得到服务。

优先队列可以使用数组或链表实现，从时间和空间复杂度来说，往往用二叉堆来实现。

Python 中提供heapq的lib来实现 priority queue.
提供push和pop两个基本操作和heapify初始化操作.
'''
import heapq
item = ['q','w','e','t','x']
priority_Q = []
heapq.heappush(priority_Q,item) # 插入操作 复杂度为 O(logN)
heapq.heappop(priority_Q) # 删除操作 复杂度为 O(logN)
heapq.heapify(priority_Q) # init操作 复杂度为 O(NlogN)
print(priority_Q[0]) # peek操作 复杂度为 O(1)


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-Deque-双端队列-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Deque - 双端队列
'''
双端队列（deque，全名double-ended queue）
可以让你在任何一端添加或者移除元素，因此它是一种具有队列和栈性质的数据结构。

Python 的list就可以执行类似于deque的操作， 但是效率会过于慢。
为了提升数据的处理效率， 一些高效的数据结构放在了collections中。
在collections 中提供了deque的类， 如果需要多次对list执行头尾元素的操作， 请使用deque。
'''
import collections
dq = collections.deque()

dq.appendleft(item) # 插入左边操作 复杂度为 O(1)
dq.append(item) # 插入右边操作 复杂度为 O(1)
dq.popleft(item) # 删除左边操作 复杂度为 O(1)
dq.pop(item) # 删除右边操作 复杂度为 O(1)
print(dq[0]) # 查看左边操作 复杂度为 O(1)
print(dq[-1]) # 查看右边操作 复杂度为 O(1)

'''
实例

二项式系数

题目
编写程序，求二项式系数表中(杨辉三角)第K层系列数

   1
  1  1
 1  2  1
1 3  3  1
......
思路

把第K行的系数存储在队列中
依次出队K层的系数（每行最后一个1不出队），并推算K+1层系数，添加到队尾，最后在队尾添加一个1，便变成了k+1行。
'''
from collections import deque
def yanghui(k):
    """
    :param k: 杨辉三角中第几层
    :return: 第K层的系数
    """
    q = deque([1])  # 创建一个队列，默认从1开始
    for i in range(k):  # 迭代要查找的层数
        for _ in range(i):  # 循环需要出队多少次
            q.append(q.popleft() + q[0])  # 第一个数加上队列中第二个数并赋值到队列末尾
        q.append(1)  # 每次查找结束后都需要在队列最右边添加个1
    return list(q)
result = yanghui(3)
print(result)

'''
划分无冲突子集

题目
某动物园搬家，要运走N种动物，老虎与狮子放在一起会大家，大象与犀牛放在一个笼子会打架，野猪和野狗放在一个笼子里会打架，现在需要我们设计一个算法，使得装进同一个笼子的动物互相不打架。

思路
把所有动物按次序入队
创建一个笼子(集合)，出队一个动物，如果和笼子内动物无冲冲突则添加到该笼子，有冲突则添加到队尾，等待进入新笼子
由于队列先进先出的特性，如果当前出队动物的index不大于前一个出队动物的index，说明当前队列中所有动物已经尝试过进入且进入不了当前笼子，此时创建信的笼子(集合)
'''
from collections import deque
def division(m, n):
    """
    :param m: 冲突关系矩阵
    :param n: 几种动物
    :return: 返回一个栈，栈内包含了所有的笼子
    """
    res = []  # 创建一个栈
    q = deque(range(n))  # 初始化队列，里面放着动物的序号
    pre = n  # 前一个动物的下标
    while q:
        cur = q.popleft()  # 从队头出队一个动物
        if pre >= cur:  # 是否需要创建笼子
            res.append([])  # 创建一个笼子
        # 当前的动物是否与笼子内的动物有冲突
        for a in res[-1]:  # 迭代栈中最顶层的笼子
            if m[cur][a]:  # 有冲突
                q.append(cur)  # 重新放入队列的尾部
                break
        else:  # 当前动物和当前笼子中的所有动物没冲突
            res[-1].append(cur)  # 当前动物放入最上面的笼子中
        pre = cur  # 当前变成之前的
    return res
N = 9
R = {  # 冲突对应关系表
    (1, 4), (4, 8), (1, 8), (1, 7),
    (8, 3), (1, 0), (0, 5), (1, 5),
    (3, 4), (5, 6), (5, 2), (6, 2), (6, 4),
}
M = [[0] * N for _ in range(N)]  # 冲洗关系矩阵M，0代表不冲突
for i, j in R:
    M[i][j] = M[j][i] = 1  # 1代表冲突
result = division(M, N)
print(result)

'''
数字变换

题目
对于一对正整数a,b,对a只能进行加1，减1，乘2操作，问最少对a进行几次操作能得到b？

例如：
a=3,b=11: 可以通过322-1，3次操作得到11；
a=5,b=8：可以通过(5-1)*2，2次操作得到8；

思路
本题用广度优先搜索，寻找a到b状态迁移最短路径，对于每个状态s，可以转换到撞到s+1,s-1,s*2:

把初始化状态a入队；
出队一个状态s，然后s+1,s-1,s*2入队；
反复循环第二步骤，直到状态s为b；
'''
from collections import deque
def atob(a, b):
    """
    :param a: 开始的数字
    :param b: 最终转换之后的数字
    :return: 最小匹配的次数
    """
    q = deque([(a, 0)])  # a=当前数字，0=操作的次数
    checked = {a}  # 已经检查过的数据
    while True:
        s, c = q.popleft()
        if s == b:
            break
        if s < b:  # 要计算的数小于计算之后的数字
            if s + 1 not in checked:  # 如果要计算的数字+1不在已检查过的数据集合中
                q.append((s + 1, c + 1))  # 要计算的数+1，转换次数+1
                checked.add(s + 1)  # 把计算过的数添加到checked集合中
            if s * 2 not in checked:
                q.append((s * 2, c + 1))
                checked.add(s * 2)
        if s > 0:  # 要计算的数大于0
            if s - 1 not in checked:
                q.append((s - 1, c + 1))
                checked.add(s - 1)
    return q.popleft()[-1]
result = atob(3, 11)
print(result)

