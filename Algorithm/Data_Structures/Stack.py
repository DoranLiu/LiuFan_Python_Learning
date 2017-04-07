'''
栈：LIFO结构，后进先出

Queue 和 Stack 在 Python 中都是有 list [] 实现的。
'''

# 类实现方法：
class Stack:
    def __init__(self):
       self.items = []
    def is_empty(self):
       return self.items == []
    def push(self, item):
       self.items.append(item)
    def pop(self):
       return self.items.pop()
    def peek(self):
       return self.items[len(self.items)-1]
    def size(self):
       return len(self.items)

s = Stack()
print('is_empty:',s.is_empty())
s.push(4)
s.push('dog')
print('peek:',s.peek())
s.push(True)
print('size:',s.size())
print('is_empty:',s.is_empty())
s.push(8.4)
print('pop:',s.pop())
print('pop:',s.pop())
print('size:',s.size())

# list 实现方法：
# list 可以很轻松实现stack，如果需要更高效的stack，可以使用deque
stack = []
print(len(stack)) # size of stack
top = stack[-1] # 栈顶元素

import collections
stack = collections.deque()
