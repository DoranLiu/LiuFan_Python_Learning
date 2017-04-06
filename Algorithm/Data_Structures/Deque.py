'''
双向队列：左右两边都可以插入和删除的队列
'''

'''
下面的实现是以右端为front，左端为rear
'''
class Deque:
   def __init__(self):
      self.items = []
   def is_empty(self):
      return self.items == []
   def add_front(self, item):
       self.items.append(item)
   def add_rear(self, item):
      self.items.insert(0,item)
   def remove_front(self):
      return self.items.pop()
   def remove_rear(self):
      return self.items.pop(0)
   def size(self):
      return len(self.items)

dq=Deque();
dq.add_front('dog');
dq.add_rear('cat');
print(dq.items)
dq.remove_front();
dq.add_front('pig');
print(dq.items)