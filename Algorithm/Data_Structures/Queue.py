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


