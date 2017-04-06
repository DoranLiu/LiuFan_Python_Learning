'''
二叉树：
一个节点最多有两个孩子节点的树。
二叉树常被用于实现二叉查找树和二叉堆。

性质：
二叉树的第i层至多有 2^(i-1) 个结点；
深度为k的二叉树至多有 2^k -1 个结点；
对任何一棵二叉树T，如果其终端结点数为 N0 ,度为2的结点数为 N2 ,则 N0 = N2 +1。因为度为1的节点对度为0的节点数目不会有影响，而每增加一个度为2度节点总的来说会相应增加一个度为0的节点。
一棵树深度为 k ，且有 2^k -1 个节点称之为满二叉树，当且仅当其每一个节点都与深度为 k 的满二叉树中序号为1至n的节点对应时，称之为完全二叉树。
如果是从0索引开始存储，那么对应于节点p的孩子节点是2p+1和2p+2两个节点，相反，节点p的父亲节点是(p-1)/2位置上的点

遍历：
1.深度优先：
先访问子节点，再访问父节点，最后访问第二个子节点。根据根节点相对于左右子节点的访问顺序又可以分为：
    - 前序 pre-order：先根 后左 再右
    - 中序 in-order： 先左后根再右
    - 后序 post-order：先左后右再根
一般使用递归，也就是栈的思想对二叉树遍历。

2.广度优先：
先访问根节点，沿着树的宽度遍历子节点，直到所有节点均被访问为止。
一般使用队列的思想对二叉树遍历。


二叉树的应用很多，比如对算术表达式建立一颗二叉树可以清楚看出表达式是如何计算的，
二叉树的变种可以得到其他的有一定特性的数据结构，例如后面的二叉堆。
二叉树的三种遍历方法(前序，中序，后序)同样有很多的应用。
'''

'''
第一种，直接使用list来实现二叉树，可读性差
'''
def binary_tree(r):
    return [r, [], []]
def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        #new_branch becomes the left node of root, and original left
        #node t becomes left node of new_branch, right node is none
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root
def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root
def get_root_val(root):
    return root[0]
def set_root_val(root, new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]

r = binary_tree(3)
insert_left(r, 4)
insert_left(r, 5)
insert_right(r, 6)
insert_right(r, 7)
print(r)
l = get_left_child(r)
print(l)
set_root_val(l, 9)
print(r)
insert_left(l, 11)
print(r)
print(get_right_child(get_right_child(r)))


'''
第二种，使用类的形式定义二叉树，可读性更好
'''
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t
    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.val = obj

    def get_root_val(self):
        return self.val

r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())


'''
二叉树遍历：

前序遍历中第一个一定是根，而后序遍历最后一个一定是根，中序遍历在得知根节点后又可进一步递归得知左右子树的根节点。
但是这种方法也是有适用范围的：元素不能重复！否则无法完成定位。
'''
class Traversal():
    def __init__(self):
        self.traverse_path = list()

    def preorder(self,root):
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



