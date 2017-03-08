#Basics Data Structure
本文档参考自[Algorithm Github](https://github.com/billryan/algorithm-exercise)

#String

- there are some python's string method

`s1 = str()`
> in python `''` or `""` is the same
`s2 = "shaunwei"` 
> return 'shaunwei'
`s2len = len(s2)`
> last 3 chars
`s2[-3:] `
> return 'wei'
`s2[5:8]`
> return 'wei'
`s3 = s2[:5]`
> return 'shaun'
`s3 += 'wei'`
> return 'shaunwei'

- list in python is same as ArrayList in java
`s2list = list(s3)`
> string at index 4
`s2[4]`
> return 'n'

- find index at first
`s2.index('w')` 
> return 5, if not found, throw ValueError
`s2.find('w')` 
> return 5, if not found, return -1”

------------------------------------------------------------------------

# Linked List

- 线性表有两种存储方式:
    1. 顺序存储结构，比如数组。
        - 顺序表的特性是随机读取，也就是访问一个元素的时间复杂度是O(1)，链式表的特性是插入和删除的时间复杂度为O(1)。
    2. 链式存储结构,比如链表。
        - 链式存储结构就是两个相邻的元素在内存中可能不是相邻的，每一个元素都有一个指针域，指针域一般是存储着到下一个元素的指针。
        - 这种存储方式的优点是定点插入和定点删除的时间复杂度为 O(1)，不会浪费太多内存，添加元素的时候才会申请内存，删除元素会释放内存。缺点是访问的时间复杂度最坏为O(n)。


- 根据指针域的不同，链表分为单向链表、双向链表、循环链表等等.

## 单向链表的实现
```
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    # in python next is a reversed word 反转单向链表
    def reverse(self, head):
        prev = None
        while head: # “访问某个节点 curt.next 时，要检验 curt 是否为 null，
            temp = head.next
            head.next = prev
            prev = head
            head = temp # “要把反转后的最后一个节点（即反转前的第一个节点）指向 null
        return prev
```

## 双向链表的实现
```
class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head): # 双向链表的反转核心在于next和prev域的交换，还需要注意的是当前节点和上一个节点的递推
        curt = None
        while head:
            curt = head
            head = curt.next
            curt.next = curt.prev
            curt.prev = head
        return curt
```


- 链表指针的鲁棒性:
    综合上面讨论的两种基本操作，链表操作时的鲁棒性问题主要包含两个情况：
    1. 当访问链表中某个节点 curt.next 时，一定要先判断 curt 是否为 null。
    2. 全部操作结束后，判断是否有环；若有环，则置其中一端为 null。

##Dummy Node
- Dummy node 是链表问题中一个重要的技巧，中文翻译叫“哑节点”或者“假人头结点”。
- Dummy node 是一个虚拟节点，也可以认为是标杆节点。
- Dummy node 就是在链表表头 head 前加一个节点指向 head，即 dummy -> head。
- Dummy node 的使用多针对单链表没有前向指针的问题，保证链表的 head 不会在删除操作中丢失。
- Dummy node 来进行head的删除操作，比如 Remove Duplicates From Sorted List II，一般的方法current = current.next 是无法删除 head 元素的，所以这个时候如果有一个dummy node在head的前面。
- 所以，当链表的 head 有可能变化（被修改或者被删除）时，使用 dummy node 可以很好的简化代码，最终返回 dummy.next 即新的链表。

##快慢指针

快慢指针也是一个可以用于很多问题的技巧。所谓快慢指针中的快慢指的是指针向前移动的步长，每次移动的步长较大即为快，步长较小即为慢，常用的快慢指针一般是在单链表中让快指针每次向前移动2，慢指针则每次向前移动1。快慢两个指针都从链表头开始遍历，于是快指针到达链表末尾的时候慢指针刚好到达中间位置，于是可以得到中间元素的值。快慢指针在链表相关问题中主要有两个应用：

快速找出未知长度单链表的中间节点 设置两个指针 *fast、*slow 都指向单链表的头节点，其中*fast的移动速度是*slow的2倍，当*fast指向末尾节点的时候，slow正好就在中间了。
判断单链表是否有环 利用快慢指针的原理，同样设置两个指针 *fast、*slow 都指向单链表的头节点，其中 *fast的移动速度是*slow的2倍。如果 *fast = NULL，说明该单链表 以 NULL结尾，不是循环链表；如果 *fast = *slow，则快指针追上慢指针，说明该链表是循环链表。

- Python实现
```
“class NodeCircle:
    def __init__(self, val):
        self.val = val
        self.next = None

    def has_circle(self, head):
        slow = head
        fast = head
        while (slow and fast):
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if fast == slow:
                break
            if fast and slow and (fast == slow):
                return True
            else:
                return False
```

------------------------------------------------------------------------

#Binary Tree - 二叉树

>二叉树是每个节点最多有两个子树的树结构，子树有左右之分，二叉树常被用于实现二叉查找树和二叉堆。

Python实现
```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None”
```

##树的遍历
从二叉树的根节点出发，节点的遍历分为三个主要步骤：
- 对当前节点进行操作（称为“访问”节点，或者根节点）、遍历左边子节点、遍历右边子节点。
访问节点顺序的不同也就形成了不同的遍历方式。需要注意的是树的遍历通常使用递归的方法进行理解和实现，在访问元素时也需要使用递归的思想去理解。
实际实现中对于前序和中序遍历可尝试使用递归实现。

按照访问根元素(当前元素)的前后顺序，遍历方式可划分为如下几种：
“深度优先：先访问子节点，再访问父节点，最后访问第二个子节点。根据根节点相对于左右子节点的访问先后顺序又可细分为以下三种方式。
前序(pre-order)：先根后左再右
中序(in-order)：先左后根再右
后序(post-order)：先左后右再根
广度优先：先访问根节点，沿着树的宽度遍历子节点，直到所有节点均被访问为止。
如下图所示，遍历顺序在右侧框中，红色A为根节点。使用递归和整体的思想去分析遍历顺序较为清晰。

二叉树的广度优先遍历和树的前序/中序/后序遍历不太一样，前/中/后序遍历使用递归，也就是栈的思想对二叉树进行遍历，广度优先一般使用队列的思想对二叉树进行遍历。

如果已知中序遍历和前序遍历或者后序遍历，那么就可以“完全恢复出原二叉树结构。其中最为关键的是前序遍历中第一个一定是根，而后序遍历最后一个一定是根，中序遍历在得知根节点后又可进一步递归得知左右子树的根节点。但是这种方法也是有适用范围的：元素不能重复！否则无法完成定位。”

```
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Traversal(object):
    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
```

##树类题的复杂度分析
- 对树相关的题进行复杂度分析时可统计对每个节点被访问的次数，进而求得总的时间复杂度。

##Binary Search Tree - 二叉查找树
- 一颗二叉查找树(BST)是一颗二叉树，其中每个节点都含有一个可进行比较的键及相应的值，且每个节点的键都大于等于左子树中的任意节点的键，而小于右子树中的任意节点的键。

使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。
二叉查找树使用的每个节点含有两个链接，它是将链表插入的灵活性和有序数组查找的高效性结合起来的高效符号表实现。

------------------------------------------------------------------------

#Huffman Compression - 霍夫曼压缩

主要思想：放弃文本文件的普通保存方式：不再使用7位或8位二进制数表示每一个字符，而是用较少的比特表示出现频率最高的字符，用较多的比特表示出现频率低的字符。

使用变长编码来表示字符串，势必会导致编解码时码字的唯一性问题，因此需要一种编解码方式唯一的前缀码，而表示前缀码的一种简单方式就是使用单词查找树，其中最优前缀码即为Huffman首创。

以符号F, O, R, G, E, T为例，其出现的频次如以下表格所示。
| ------------- |:-------------:| -----:|
|Symbol	| F	| O | R	| G	| E	| T |
|Frequence	| 2	| 3	| 4	| 4	| 5 | 7 |
|Code | 000	| 001 | 100	| 101 | 01 | 10|
则对各符号进行霍夫曼编码的动态演示如下图所示。基本步骤是将出现频率由小到大排列，组成子树后频率相加作为整体再[…]”

```
“""
Use serveral ways to compress string `everyday is awesome!`
1. use simple bits to replace ASCII value
2. use huffman coding
"""
import heapq
import collections


def get_rate(compressed_binary, uncompressed_bits):
    return len(compressed_binary) * 100 / uncompressed_bits

class SimpleCompression:
    def __init__(self, string):
        self.symbols = set(string)
        self.bit_len = 1
        while 2**self.bit_len < len(self.symbols):
            self.bit_len += 1
        self.string = string

        self.s2b = {}
        self.b2s = {}
        i = 0
        for s in self.symbols:
            b = bin(i)[2:]
            if len(b) < self.bit_len:
                b = (self.bit_len - len(b)) * '0' + b
            self.s2b[s] = b
            self.b2s[b] = s
            i += 1

    def compress(self):
        bits = ''
        for s in self.string:
            bits += self.s2b[s]
        return bits
    def uncompress(self, bits):
        string = ''
        for i in xrange(0, len(bits), self.bit_len):
            string += self.b2s[bits[i:i + self.bit_len]]
        return string


class HuffmanCompression:
    class Trie:
        def __init__(self, val, char=''):
            self.val = val
            self.char = char
            self.coding = ''
            self.left = self.right = None

        def __cmp__(self, other):
            return self.val - other.val

    def __init__(self, string):
        self.string = string
        counter = collections.Counter(string)
        heap = []
        for char, cnt in counter.items():
            heapq.heappush(heap, HuffmanCompression.Trie(cnt, char))

        while len(heap) != 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            trie = HuffmanCompression.Trie(left.val + right.val)
            trie.left, trie.right = left, right
            heapq.heappush(heap, trie)

        self.root = heap[0]
        self.s2b = {}
        self.bfs_encode(self.root, self.s2b)

    def bfs_encode(self, root, s2b):
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.char:
                s2b[node.char] = node.coding
                continue
            if node.left:
                node.left.coding = node.coding + '0'
                queue.append(node.left)
            if node.right:
                node.right.coding = node.coding + '1'
                queue.append(node.right)

    def compress(self):
        bits = ''
        for char in self.string:
            bits += self.s2b[char]
        return bits

    def uncompress(self, bits):
        string = ''
        root = self.root
        for bit in bits:
            if bit == '0':
                root = root.left
            else:
                root = root.right
            if root.char:
                string += root.char
                root = self.root
        return string


if __name__ == '__main__':
    s = 'everyday is awesome!'
    # ASCII
    bits = len(s) * 8
    print('Total bits: %d' % bits)

    # simple compression
    sc = SimpleCompression(s)
    compressed = sc.compress()
    print('Compressed binary: ' + compressed)
    print('Uncompressed: ' + sc.uncompress(compressed))
    print(sc.s2b)
    print('Simple Compression-compress rate: %d%%' % get_rate(compressed, bits))
    print('===================')
    # huffman compression
    hc = HuffmanCompression(s)
    compressed = hc.compress()
    print('Compressed binary: ' + compressed)
    print('Uncompressed: ' + hc.uncompress(compressed))
    print(hc.s2b)
    print('Huffman Compression-compress rate: %d%%' % get_rate(compressed, bits))

"""
Total bits: 160
Compressed binary: 00101011001010001100001100001100000101000111000100001010001001110110010100101001
Uncompressed: everyday is awesome!
{'a': '0000', ' ': '0001', 'e': '0010', 'd': '0011', 'i': '0100', 'm': '0101', 'o': '0110', 's': '0111', 'r': 1000', '!': '1001', 'w': '1010', 'v': '1011', 'y': '1100'}
Simple Compression-compress rate: 50%
===================
Compressed binary: 011001011011110011010111111000010000111000111111010011110100011011010001
Uncompressed: everyday is awesome!
{'!': '0001', ' ': '001', 'e': '01', 'd': '11010', 'i': '0000', 'm': '11011', 'o': '1000', 's': '1110', 'r': '1011', 'a': '1111', 'w': '1010', 'v': '1001', 'y': '1100'}
Huffman Compression-compress rate: 45%
""”
```

###源码分析
- 简单压缩： 根据字符串出现的字符，将ASCII替换成更短的表示形式 
- 霍夫曼压缩： 根据字符串出现频率，构建Trie树， 对每个tree node进行定义，使得频率越高的字符离root节点越近
有关霍夫曼编码的具体步骤可参考 [Huffman 编码压缩算法 | 酷 壳 - CoolShell.cn](http://coolshell.cn/articles/7459.html) 和 [霍夫曼编码 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E9%9C%8D%E5%A4%AB%E6%9B%BC%E7%BC%96%E7%A0%81)，清晰易懂。

------------------------------------------------------------------------

#Queue
Queue 是一个 FIFO（先进先出）的数据结构，并发中使用较多，可以安全地将对象从一个任务传给另一个任务。

Python编程实现

Queue 和 Stack 在 Python 中都是有 list ,[] 实现的。 在python 中list是一个dynamic array, 可以通过append在list的尾部添加元素， 通过pop()在list的尾部弹出元素实现Stack的FILO， 如果是pop(0)则弹出头部的元素实现Queue的FIFO。

```
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
queue[0] # return 2 examine the first element
```

###Methods
Insert	queue.append(e)
Remove	queue.pop(0)
Examine	queue[0]

## Priority Queue - 优先队列
应用程序常常需要处理带有优先级的业务，优先级最高的业务首先得到服务。因此优先队列这种数据结构应运而生。优先队列中的每个元素都有各自的优先级，优先级最高的元素最先得到服务；优先级相同的元素按照其在优先队列中的顺序得到服务。
优先队列可以使用数组或链表实现，从时间和空间复杂度来说，往往用二叉堆来实现。

Python
Python 中提供heapq的lib来实现 priority queue. 提供push和pop两个基本操作和heapify初始化操作.
enqueue	heapq.push(queue, e)
dequeue	heapq.pop(queue)
init	heapq.heapify(queue)
peek	queue[0]

##Deque - 双端队列

双端队列（deque，全名double-ended queue）可以让你在任何一端添加或者移除元素，因此它是一种具有队列和栈性质的数据结构。

Python 的list就可以执行类似于deque的操作， 但是效率会过于慢。 为了提升数据的处理效率， 一些高效的数据结构放在了collections中。 在collections 中提供了deque的类， 如果需要多次对list执行头尾元素的操作， 请使用deque。
dq = collections.deque();

###Methods
enqueue left	dq.appendleft(e)
enqueue right	dq.append(e)
dequeue left	dq.popleft()
dequeue right	dq.pop()
peek left	dq[0]
peek right	dq[-1]

##Referce:
[優先佇列 - 维基百科，自由的百科全书](https://zh.wikipedia.org/zh/%E5%84%AA%E5%85%88%E4%BD%87%E5%88%97)
[双端队列 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)

------------------------------------------------------------------------

#Heap - 堆

一般情况下，堆通常指的是二叉堆，二叉堆是一个近似完全二叉树的数据结构，即披着二叉树羊皮的数组，故使用数组来实现较为便利。子结点的键值或索引总是小于（或者大于）它的父节点，且每个节点的左右子树又是一个二叉堆(大根堆或者小根堆)。根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常被用作实现优先队列。

##特点
以数组表示，但是以完全二叉树的方式理解。
唯一能够同时最优地利用空间和时间的方法——最坏情况下也能保证使用 2NlogN 次比较和恒定的额外空间。
在索引从0开始的数组中：
父节点 i 的左子节点在位置(2*i+1)
父节点 i 的右子节点在位置(2*i+2)
子节点 i 的父节点在位置floor((i-1)/2)

堆的基本操作
以大根堆为例，堆的常用操作如下。
最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
创建最大堆（Build_Max_Heap）：将堆所有数据重新排序
堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的递归运算
其中步骤1是给步骤2和3用的。

Python实现
```
class MaxHeap:
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _sink(self, array, i):
        # move node down the tree
        left, right = 2 * i + 1, 2 * i + 2
        max_index = i
        if left < len(array) and array[left] > array[max_index]:
            max_index = left
        if right < len(array) and array[right] > array[max_index]:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)
    
    def _swim(self, array, i):
        # move node up the tree
        if i == 0:
            return
        father = (i - 1) / 2
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)

    def _max_heapify(self, array):
        for i in xrange(len(array) / 2, -1, -1):
            self._sink(array, i)
        return array

    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        “item = self.heap.pop()
        self._sink(self.heap, 0)
        return item
```

------------------------------------------------------------------------

#Stack - 栈
栈是一种 LIFO(Last In First Out) 的数据结构，常用方法有添加元素，取栈顶元素，弹出栈顶元素，判断栈是否为空。

Python
```
stack = []
len(stack) # size of stack

# more efficient stack
import collections
stack = collections.deque()
```

list作为最基本的python数据结构之一， 可以很轻松的实现stack。 如果需要更高效的stack， 建议使用deque。

###Methods
len(stack) != 0 -- 判断stack是否weikong
stack[-1] -- 取栈顶元素，不移除
pop() -- 移除栈顶元素并返回该元素
append(item) -- 向栈顶添加元素”

------------------------------------------------------------------------

#Set

Set 是一种用于保存不重复元素的数据结构。常被用作测试归属性，故其查找的性能十分重要。

Python实现
Set 是python自带的基本数据结构， 有多种初始化方式。 Python的set跟dict的Implementation方式类似， 可以认为set是只有key的dict.
```
s = set()
s1 = {1, 2, 3}
s.add('shaunwei')
'shaun' in s  # return true
s.remove('shaunwei')
```

------------------------------------------------------------------------

#Map - 哈希表
Map 是一种关联数组的数据结构，也常被称为字典或键值对。

Python实现
在 Python 中 dict(Map) 是一种基本的数据结构。
```
# map 在 python 中是一个keyword
hash_map = {} # or dict()
hash_map['shaun'] = 98
hash_map['wei'] = 99
exist = 'wei' in hash_map  # check existence
point = hash_map['shaun']  # get value by key
point = hash_map.pop('shaun') # remove by key, return value
keys = hash_map.keys()  # return key list
# iterate dictionary(map)
for key, value in hash_map.items():
    # do something with k, v
    pass”
```

------------------------------------------------------------------------

#Graph - 图
图的表示通常使用邻接矩阵和邻接表，前者易实现但是对于稀疏矩阵会浪费较多空间，后者使用链表的方式存储信息但是对于图搜索时间复杂度较高。

###编程实现

###邻接矩阵
设顶点个数为 V, 那么邻接矩阵可以使用 V × V 的二维数组来表示。 g[i][j]表示顶点i和顶点j的关系，对于无向图可以使用0/1表示是否有连接，对于带权图则需要使用INF来区分。有重边时保存边数或者权值最大/小的边即可。
```
g = [[0 for _ in range(V)] for _ in range(V)]
```

###邻接表
邻接表通过表示从顶点i出发到其他所有可能能到的边。
- 有向图
```
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
```

- 无向图同上，只不过在建图时双向同时加。
```
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
```

------------------------------------------------------------------------

