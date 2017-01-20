#Linked List - 链表（一）

#本节包含链表的一些常用操作，如删除、插入和合并等。
#常见错误有 遍历链表不向前递推节点，遍历链表前未保存头节点，返回链表节点指针错误。


'''
Question
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.
Example

Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''
#题解
#遍历之，遇到当前节点和下一节点的值相同时，删除下一节点，并将当前节点next值指向下一个节点的next, 当前节点首先保持不变，直到相邻节点的值不等时才移动到下一节点。

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def deleteDuplicates(self, head):
    curt = head
    while curt:
        while curt.next and curt.next.val == curt.val:
            curt.next = curt.next.next
        curt = curt.next
    return head

#源码分析
#    首先进行异常处理，判断head是否为NULL
#    遍历链表，curr->val == curr->next->val时，保存curr->next，便于后面释放内存(非C/C++无需手动管理内存)
#    不相等时移动当前节点至下一节点，注意这个步骤必须包含在else中，否则逻辑较为复杂
#while 循环处也可使用curr != null && curr.next != null, 这样就不用单独判断head 是否为空了，但是这样会降低遍历的效率，因为需要判断两处。使用双重while循环可只在内循环处判断，避免了冗余的判断，谢谢 @xuewei4d 提供的思路。

#复杂度分析
#遍历链表一次，时间复杂度为 O(n)O(n)O(n), 使用了一个中间变量进行遍历，空间复杂度为 O(1)O(1)O(1).

'''
Question

Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Example

Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

#题解
#上题为保留重复值节点的一个，这题删除全部重复节点，看似区别不大，但是考虑到链表头不确定(可能被删除，也可能保留)，因此若用传统方式需要较多的if条件语句。这里介绍一个处理链表头节点不确定的方法——引入dummy node.
#ListNode *dummy = new ListNode(0);
#dummy->next = head;
#ListNode *node = dummy;
#引入新的指针变量dummy，并将其next变量赋值为head，考虑到原来的链表头节点可能被删除，故应该从dummy处开始处理，这里复用了head变量。考虑链表A->B->C，删除B时，需要处理和考虑的是A和C，将A的next指向C。如果从空间使用效率考虑，可以使用head代替以上的node，含义一样，node比较好理解点。
#与上题不同的是，由于此题引入了新的节点dummy，不可再使用node->val == node->next->val，原因有二：
#    此题需要将值相等的节点全部删掉，而删除链表的操作与节点前后两个节点都有关系，故需要涉及三个链表节点。且删除单向链表节点时不能删除当前节点，只能改变当前节点的next指向的节点。
#    在判断val是否相等时需先确定node->next和node->next->next均不为空，否则不可对其进行取值。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def deleteDuplicates(self, head):
    if head is None:
        return None

    dummy = ListNode(0)
    dummy.next = head
    node = dummy
    while node.next is not None and node.next.next is not None:
        if node.next.val == node.next.next.val:
            val_prev = node.next.val
            while node.next is not None and node.next.val == val_prev:
                node.next = node.next.next
        else:
            node = node.next

    return dummy.next

#源码分析
#    首先考虑异常情况，head 为 NULL 时返回 NULL
#    new一个dummy变量，dummy->next指向原链表头。(C++中最好不要使用 new 的方式生成 dummy, 否则会有内存泄露)
#    使用新变量node并设置其为dummy头节点，遍历用。
#    当前节点和下一节点val相同时先保存当前值，便于while循环终止条件判断和删除节点。注意这一段代码也比较精炼。
#    最后返回dummy->next，即题目所要求的头节点。

#Python 中也可不使用is not None判断，但是效率会低一点。
#复杂度分析
#两根指针(node.next 和 node.next.next)遍历，时间复杂度为 O(2n)O(2n)O(2n). 使用了一个 dummy 和中间缓存变量，空间复杂度近似为 O(1)O(1)O(1).

'''
Question

Partition List
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
#题解
#此题出自 CTCI 题 2.4，依据题意，是要根据值x对链表进行分割操作，具体是指将所有小于x的节点放到不小于x的节点之前，咋一看和快速排序的分割有些类似，但是这个题的不同之处在于只要求将小于x的节点放到前面，而并不要求对元素进行排序。
#这种分割的题使用两路指针即可轻松解决。左边指针指向小于x的节点，右边指针指向不小于x的节点。由于左右头节点不确定，我们可以使用两个dummy节点。
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def partition(self, head, x):
    if head is None:
        return None

    leftDummy = ListNode(0)
    left = leftDummy
    rightDummy = ListNode(0)
    right = rightDummy
    node = head
    while node is not None:
        if node.val < x:
            left.next = node
            left = left.next
        else:
            right.next = node
            right = right.next
        node = node.next
    # post-processing
    right.next = None
    left.next = rightDummy.next

    return leftDummy.next

#源码分析
#    异常处理
#    引入左右两个dummy节点及left和right左右尾指针
#    遍历原链表
#    处理右链表，置right->next为空(否则如果不为尾节点则会报错，处理链表时 以 null 为判断)，将右链表的头部链接到左链表尾指针的next，返回左链表的头部

#复杂度分析
#遍历链表一次，时间复杂度近似为 O(n)O(n)O(n), 使用了两个 dummy 节点及中间变量，空间复杂度近似为 O(1)O(1)O(1).

'''
Question

Add Two Numbers:
You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.
Example

Given 7->1->6 + 5->9->2. That is, 617 + 295.

Return 2->1->9. That is 912.

Given 3->1->5 and 5->9->2, return 8->0->8.
'''

#题解
#一道看似简单的进位加法题，实则杀机重重，不信你不看答案自己先做做看。
#首先由十进制加法可知应该注意进位的处理，但是这道题仅注意到这点就够了吗？还不够！因为两个链表长度有可能不等长！因此这道题的亮点在于边界和异常条件的处理，感谢 @wen 引入的 dummy 节点，处理起来更为优雅！

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def add_two_numbers(self, l1, l2):
    '''
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    '''
    carry = 0
    dummy = prev = ListNode(-1)
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) / 10

        prev.next = ListNode(val)
        prev = prev.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy.next

#源码分析
#    迭代能正常进行的条件为(NULL != l1) || (NULL != l2) || (0 != carry), 缺一不可。
#    对于空指针节点的处理可以用相对优雅的方式处理 - int l1_val = (NULL == l1) ? 0 : l1->val;
#    生成新节点时需要先判断迭代终止条件 - (NULL == l1) && (NULL == l2) && (0 == carry), 避免多生成一位数0。 使用 dummy 节点可避免这一情况。

#复杂度分析
#没啥好分析的，时间和空间复杂度均为 O(max(L1,L2))O(max(L1, L2))O(max(L1,L2)).

'''
Question

Linked List Cycle:
Given a linked list, determine if it has a cycle in it.

Example
Given -21->10->4->5, tail connects to node index 1, return true
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def hasCycle(self, head):
    # write your code here
    if head is None:
        return False
    p1 = head
    p2 = head
    while True:
        if p1.next is not None:
            p1=p1.next.next
            p2=p2.next
            if p1 is None or p2 is None:
                return False
            elif p1 == p2:
                return True
        else:
            return False
    return False
#源码分析
#    异常处理，将head->next也考虑在内有助于简化后面的代码。
#    慢指针初始化为head, 快指针初始化为head的下一个节点，这是快慢指针初始化的一种方法，有时会简化边界处理，但有时会增加麻烦，比如该题的进阶版。

#复杂度分析
#    在无环时，快指针每次走两步走到尾部节点，遍历的时间复杂度为 O(n/2)O(n/2)O(n/2).
#    有环时，最坏的时间复杂度近似为 O(n)O(n)O(n). 最坏情况下链表的头尾相接，此时快指针恰好在慢指针前一个节点，还需 n 次快慢指针相遇。最好情况和无环相同，尾节点出现环。
#故总的时间复杂度可近似为 O(n)O(n)O(n).

'''
Question

Reverse Linked List
Example
For linked list 1->2->3, the reversed linked list is 3->2->1
'''

#题解1 - 非递归
#联想到同样也可能需要翻转的数组，在数组中由于可以利用下标随机访问，翻转时使用下标即可完成。而在单向链表中，仅仅只知道头节点，而且只能单向往前走，故需另寻出路。分析由1->2->3变为3->2->1的过程，由于是单向链表，故只能由1开始遍历，1和2最开始的位置是1->2，最后变为2->1，故从这里开始寻找突破口，探讨如何交换1和2的节点。
#temp = head->next;
#head->next = prev;
#prev = head;
#head = temp;

#要点在于维护两个指针变量prev和head, 翻转相邻两个节点之前保存下一节点的值，分析如下图所示：
#    保存head下一节点
#    将head所指向的下一节点改为prev
#    将prev替换为head，波浪式前进
#    将第一步保存的下一节点替换为head，用于下一次循环

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def reverseList(self, head):
    prev = None
    curr = head
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    # fix head
    head = prev

    return head

#源码分析
#题解中基本分析完毕，代码中的prev赋值比较精炼，值得借鉴。
#复杂度分析
#遍历一次链表，时间复杂度为 O(n)O(n)O(n), 使用了辅助变量，空间复杂度 O(1)O(1)O(1).

#题解2 - 递归
#递归的终止步分三种情况讨论：
#    原链表为空，直接返回空链表即可。
#    原链表仅有一个元素，返回该元素。
#    原链表有两个以上元素，由于是单链表，故翻转需要自尾部向首部逆推。
#由尾部向首部逆推时大致步骤为先翻转当前节点和下一节点，然后将当前节点指向的下一节点置空(否则会出现死循环和新生成的链表尾节点不指向空)，如此递归到头节点为止。新链表的头节点在整个递归过程中一直没有变化，逐层向上返回。

"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def reverse(self, head):
    # case1: empty list
    if head is None:
        return head
    # case2: only one element list
    if head.next is None:
        return head
    # case3: reverse from the rest after head
    newHead = self.reverse(head.next)
    # reverse between head and head->next
    head.next.next = head
    # unlink list from the rest
    head.next = None

    return newHead

#源码分析
#case1 和 case2 可以合在一起考虑，case3 返回的为新链表的头节点，整个递归过程中保持不变。
#复杂度分析
#递归嵌套层数为 O(n)O(n)O(n), 时间复杂度为 O(n)O(n)O(n), 空间(不含栈空间)复杂度为 O(1)O(1)O(1).

'''
Question

Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer
which could point to any node in the list or null.

Return a deep copy of the list.
'''
#题解1 - 哈希表(两次遍历)
#首先得弄懂深拷贝的含义，深拷贝可不是我们平时见到的对基本类型的变量赋值那么简单，深拷贝常常用于对象的克隆。这道题要求深度拷贝一个带有 random 指针的链表，random 可能指向空，也可能指向链表中的任意一个节点。
#对于通常的单向链表，我们依次遍历并根据原链表的值生成新节点即可，原链表的所有内容便被复制了一份。但由于此题中的链表不只是有 next 指针，还有一个随机指针，故除了复制通常的 next 指针外还需维护新链表中的随机指针。容易混淆的地方在于原链表中的随机指针指向的是原链表中的节点，深拷贝则要求将随机指针指向新链表中的节点。
#所有类似的深度拷贝题目的传统做法，都是维护一个 hash table。即先按照复制一个正常链表的方式复制，复制的时候把复制的结点做一个 hash table，以旧结点为 key，新节点为 value。这么做的目的是为了第二遍扫描的时候我们按照这个哈希表把结点的 random 指针接上。
'''
原链表和深拷贝之后的链表如下：

|------------|             |------------|
|            v       ===>  |            v
1  --> 2 --> 3 --> 4       1' --> 2'--> 3'--> 4'

深拷贝步骤如下；

    根据 next 指针新建链表
    维护新旧节点的映射关系
    拷贝旧链表中的 random 指针
    更新新链表中的 random 指针

其中1, 2, 3 可以合并在一起。
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

def copyRandomList(self, head):
    dummy = RandomListNode(0)
    curNode = dummy
    randomMap = {}

    while head is not None:
        # link newNode to new List
        newNode = RandomListNode(head.label)
        curNode.next = newNode
        # map old node head to newNode
        randomMap[head] = newNode
        # copy old node random pointer
        newNode.random = head.random
        #
        head = head.next
        curNode = curNode.next

    # re-mapping old random node to new node
    curNode = dummy.next
    while curNode is not None:
        if curNode.random is not None:
            curNode.random = randomMap[curNode.random]
        curNode = curNode.next

    return dummy.next

#源码分析
#    只需要一个 dummy 存储新的拷贝出来的链表头，以用来第二次遍历时链接 random 指针。所以第一句异常检测可有可无。
#    第一次链接时勿忘记同时拷贝 random 指针，但此时的 random 指针并没有真正“链接”上，实际上是链接到了原始链表的 node 上。
#    第二次遍历是为了把原始链表的被链接的 node 映射到新链表中的 node，从而完成真正“链接”。

#复杂度分析
#总共要进行两次扫描，所以时间复杂度是 O(2n)=O(n)O(2n)=O(n)O(2n)=O(n), 在链表较长时可能会 TLE(比如 Python). 空间上需要一个哈希表来做结点的映射，所以空间复杂度也是 O(n)O(n)O(n).

#题解2 - 哈希表(一次遍历)
#从题解1 的分析中我们可以看到对于 random 指针我们是在第二次遍历时单独处理的，那么在借助哈希表的情况下有没有可能一次遍历就完成呢？我们回想一下题解1 中random 节点的处理，由于在第一次遍历完之前 random 所指向的节点是不知道到底是指向哪一个节点，故我们在将 random 指向的节点加入哈希表之前判断一次就好了(是否已经生成，避免对同一个值产生两个不同的节点)。由于 random 节点也在第一次遍历加入哈希表中，故生成新节点时也需要判断哈希表中是否已经存在。

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
def copyRandomList(self, head):
    dummy = RandomListNode(0)
    curNode = dummy
    hash_map = {}

    while head is not None:
        # link newNode to new List
        if head in hash_map.keys():
            newNode = hash_map[head]
        else:
            newNode = RandomListNode(head.label)
            hash_map[head] = newNode
        curNode.next = newNode
        # map old node head to newNode
        hash_map[head] = newNode
        # copy old node random pointer
        if head.random is not None:
            if head.random in hash_map.keys():
                newNode.random = hash_map[head.random]
            else:
                newNode.random = RandomListNode(head.random.label)
                hash_map[head.random] = newNode.random
        #
        head = head.next
        curNode = curNode.next

    return dummy.next

#源码分析
#随机指针指向节点不定，故加入哈希表之前判断一下 key 是否存在即可。C++ 中 C++ 11 引入的 unordered_map 较 map 性能更佳，使用 count 判断 key 是否存在比 find 开销小一点，因为 find 需要构造 iterator。

#复杂度分析
#遍历一次原链表，判断哈希表中 key 是否存在，故时间复杂度为 O(n)O(n)O(n), 空间复杂度为 O(n)O(n)O(n).

#题解3 - 间接使用哈希表
#上面的解法很显然，需要额外的空间。这个额外的空间是由 hash table 的维护造成的。因为当我们访问一个结点时可能它的 random 指针指向的结点还没有访问过，结点还没有创建，所以需要用 hash table 的额外线性空间维护。
#但我们可以通过链表原来结构中的 next 指针来替代 hash table 做哈希。假设有如下链表：
'''
|------------|
|            v
1  --> 2 --> 3 --> 4

节点1的 random 指向了3。首先我们可以通过 next 遍历链表，依次拷贝节点，并将其添加到原节点后面，如下：

|--------------------------|
|                          v
1  --> 1' --> 2 --> 2' --> 3 --> 3' --> 4 --> 4'
       |                   ^
       |-------------------|

因为我们只是简单的复制了 random 指针，所以新的节点的 random 指向的仍然是老的节点，譬如上面的1和1'都是指向的3。

调整新的节点的 random 指针，对于上面例子来说，我们需要将1'的 random 指向3'，其实也就是原先 random 指针的next节点。

|--------------------------|
|                          v
1  --> 1' --> 2 --> 2' --> 3 --> 3' --> 4 --> 4'
       |                         ^
       |-------------------------|

最后，拆分链表，就可以得到深度拷贝的链表了。
'''
#总结起来，实际我们对链表进行了三次扫描，第一次扫描对每个结点进行复制，然后把复制出来的新节点接在原结点的 next 指针上，也就是让链表变成一个重复链表，就是新旧更替；第二次扫描中我们把旧结点的随机指针赋给新节点的随机指针，因为新结点都跟在旧结点的下一个，所以赋值比较简单，就是 node->next->random = node->random->next，其中 node->next 就是新结点，因为第一次扫描我们就是把新结点接在旧结点后面。现在我们把结点的随机指针都接好了，最后一次扫描我们把链表拆成两个，第一个还原原链表，而第二个就是我们要求的复制链表。因为现在链表是旧新更替，只要把每隔两个结点分别相连，对链表进行分割即可。

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

def copyRandomList(self, head):
    if head is None:
        return None

    curr = head
    # step1: generate new List with node
    while curr is not None:
        newNode = RandomListNode(curr.label)
        newNode.next = curr.next
        curr.next = newNode
        curr = curr.next.next

    # step2: copy random pointer
    curr = head
    while curr is not None:
        if curr.random is not None:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # step3: split original and new List
    newHead = head.next
    curr = head
    while curr is not None:
        newNode = curr.next
        curr.next = curr.next.next
        if newNode.next is not None:
            newNode.next = newNode.next.next
        curr = curr.next

    return newHead

#源码分析
#注意指针使用前需要判断是否非空，迭代时注意是否前进两步，即.next.next
#复杂度分析
#总共进行三次线性扫描，所以时间复杂度是 O(n)O(n)O(n)。但不再需要额外空间的 hash table，所以空间复杂度是 O(1)O(1)O(1)。

'''
Question

Insertion Sort List
Sort a linked list using insertion sort.

Example
Given 1->3->2->0->null, return 0->1->2->3->null.
'''

#题解1 - 从首到尾遍历
#插入排序常见的实现是针对数组的，如前几章总的的 Insertion Sort，但这道题中的排序的数据结构为单向链表，故无法再从后往前遍历比较值的大小了。好在天无绝人之路，我们还可以从前往后依次遍历比较和交换。
#由于排序后头节点不一定，故需要引入 dummy 大法，并以此节点的next作为最后返回结果的头节点，返回的链表从dummy->next这里开始构建。首先我们每次都从dummy->next开始遍历，依次和上一轮处理到的节点的值进行比较，直至找到不小于上一轮节点值的节点为止，随后将上一轮节点插入到当前遍历的节点之前，依此类推。文字描述起来可能比较模糊，大家可以结合以下的代码在纸上分析下。

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def insertionSortList(self, head):
    dummy = ListNode(0)
    cur = head
    while cur is not None:
        pre = dummy
        while pre.next is not None and pre.next.val < cur.val:
            pre = pre.next
        temp = cur.next
        cur.next = pre.next
        pre.next = cur
        cur = temp
    return dummy.next

#源码分析
#    新建 dummy 节点，用以处理最终返回结果中头节点不定的情况。
#    以cur表示当前正在处理的节点，在从 dummy 开始遍历前保存cur的下一个节点作为下一轮的cur.
#    以pre作为遍历节点，直到找到不小于cur值的节点为止。
#    将pre的下一个节点pre->next链接到cur->next上，cur链接到pre->next, 最后将cur指向下一个节点。
#    返回dummy->next最为最终头节点。

#Python 的实现在 lintcode 上会提示 TLE, leetcode 上勉强通过，这里需要注意的是采用if A is not None:的效率要比if A:高，不然 leetcode 上也过不了。具体原因可参考 Stack Overflow 上的讨论。
#复杂度分析
#最好情况：原链表已经有序，每得到一个新节点都需要 iii 次比较和一次交换, 时间复杂度为 1/2O(n2)+O(n)1/2O(n^2) + O(n)1/2O(n​2​​)+O(n), 使用了 dummy 和 pre, 空间复杂度近似为 O(1)O(1)O(1).
#最坏情况：原链表正好逆序，由于是单向链表只能从前往后依次遍历，交换和比较次数均为 1/2O(n2)1/2 O(n^2)1/2O(n​2​​), 总的时间复杂度近似为 O(n2)O(n^2)O(n​2​​), 空间复杂度同上，近似为 O(1)O(1)O(1).

#题解2 - 优化有序链表
#从题解1的复杂度分析可以看出其在最好情况下时间复杂度都为 O(n2)O(n^2)O(n​2​​) ，这显然是需要优化的。 仔细观察可发现最好情况下的比较次数 是可以优化到 O(n)O(n)O(n) 的。思路自然就是先判断链表是否有序，仅对降序的部分进行处理。优化之后的代码就没题解1那么容易写对了，建议画个图自行纸上分析下。

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
def insertionSortList(self, head):
    dummy = ListNode(0)
    dummy.next = head
    cur = head
    while cur is not None:
        if cur.next is not None and cur.next.val < cur.val:
            # find insert position for smaller(cur->next)
            pre = dummy
            while pre.next is not None and pre.next.val < cur.next.val:
                pre = pre.next
            # insert cur->next after pre
            temp = pre.next
            pre.next = cur.next
            cur.next = cur.next.next
            pre.next.next = temp
        else:
            cur = cur.next
    return dummy.next

#源码分析
#    新建 dummy 节点并将其next 指向head
#    分情况讨论，仅需要处理逆序部分。
#    由于已经确认链表逆序，故仅需将较小值(cur->next而不是cur)的节点插入到链表的合适位置。
#    将cur->next插入到pre之后，这里需要四个步骤，需要特别小心！

#复杂度分析
#最好情况下时间复杂度降至 O(n), 其他同题解1.

'''
Question

Palindrome Linked List
Implement a function to check if a linked list is a palindrome.

Example
Given 1->2->1, return true
'''

#题解1 - 使用辅助栈
#根据栈的特性(FILO)，可以首先遍历链表并入栈(最后访问栈时则反过来了)，随后再次遍历链表并比较当前节点和栈顶元素，若比较结果完全相同则为回文。 又根据回文的特性，实际上还可以只遍历链表前半部分节点，再用栈中的元素和后半部分元素进行比较，分链表节点个数为奇数或者偶数考虑即可。由于链表长度未知，因此可以考虑使用快慢指针求得。

## Definition for singly-linked list
# class ListNode:
#    def __init__(self, val):
#        self.val = val
#        self.next = None

def is_palindrome(self, head):
    if not head or not head.next:
        return True

    stack = []
    slow, fast = head, head.next
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    # for even numbers add mid
    if fast:
        stack.append(slow.val)

    curt = slow.next
    while curt:
        if curt.val != stack.pop():
            return False
        curt = curt.next
    return True

#源码分析
#注意， 在python code中， slow 和 fast pointer 分别指向head 和head.next。 这样指向的好处是：当linked－list 有奇数个数字的时候， 最终位置，slow会停在mid的位置， 而fast指向空。 当linked－list有偶数个node时， 最终位置，slow和slow.next为中间的两个元素， fast指向最后一个node。所以slow的最终位置总是mid 或者mid 偏左一点的位置。这样的位置非常方便分割linked－list，以及其他计算。推荐采用这种方法来寻找linked－list的mid位置。模版优势，请见solution2。

#复杂度分析
#使用了栈作为辅助空间，空间复杂度为 O(12n)O(\frac{1}{2}n)O(​2​​1​​n), 分别遍历链表的前半部分和后半部分，时间复杂度为 O(n)O(n)O(n).

#题解2 - 原地翻转
#题解 1 的解法使用了辅助空间，在可以改变原来的链表的基础上，可使用原地翻转，思路为翻转前半部分，然后迭代比较。具体可分为以下四个步骤。
#    找中点。
#    翻转链表的后半部分。
#    逐个比较前后部分节点值。
#    链表复原，翻转后半部分链表。

# class ListNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
def is_palindrome(self, head):
    if not head or not head.next:
        return True

    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    mid = slow.next
    # break
    slow.next = None
    rhead = self.reverse(mid)
    while rhead:
        if rhead.val != head.val:
            return False
        rhead = rhead.next
        head = head.next
    return True

def reverse(self, head):
    dummy = ListNode(-1)
    while head:
        temp = head.next
        head.next = dummy.next
        dummy.next = head
        head = temp
    return dummy.next

#源码分析
#对比Java code， 会发现，把slow 和fast pointer 放在head和head.next减少了对odd 或者even number的判断。因为slow总是在mid的位置或者mid偏左的位置上， 所以把mid assign 为slow.next总是对的。

#复杂度分析
#遍历链表若干次，时间复杂度近似为 O(n)O(n)O(n), 使用了几个临时遍历，空间复杂度为 O(1)O(1)O(1).

#题解3 - 递归(TLE)
#递归需要两个重要条件，递归步的建立和递归终止条件。对于回文比较，理所当然应该递归比较第 i 个节点和第 n-i 个节点，那么问题来了，如何构建这个递归步？大致可以猜想出来递归的传入参数应该包含两个节点，用以指代第 i 个节点和第 n-i 个节点。返回参数应该包含布尔值(用以提前返回不是回文的情况)和左半部分节点的下一个节点(用以和右半部分的节点进行比较)。由于需要返回两个值，在 Java 中需要使用自定义类进行封装，C/C++ 中则可以使用指针改变在递归调用后进行比较时节点的值。

def is_palindrome(self, head):
    result = [head, True]
    self.helper(head, result)
    return result[1]

def helper(self, right, result):
    if right:
        self.helper(right.next, result)
        is_pal =  result[0].val == right.val and result[1]
        result = [result[0].next, is_pal]

#源码分析
#核心代码为如何在递归中推进左半部分节点而对右半部分使用栈的方式逆向获取节点。左半部分的推进需要借助辅助数据结构Result.
#复杂度分析
#递归调用 n 层，时间复杂度近似为 O(n), 使用了几个临时变量，空间复杂度为 O(1).

'''
Question

Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given 1->2->3->3->4->5->3, val = 3, you should return the list as 1->2->4->5
'''

#题解
#删除链表中指定值，找到其前一个节点即可，将 next 指向下一个节点即可。

def removeElements(self, head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy
    while curr.next is not None:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next

#源码分析
#while 循环中使用curr.next较为方便，if 语句中比较时也使用curr.next.val也比较简洁，如果使用curr会比较难处理。


