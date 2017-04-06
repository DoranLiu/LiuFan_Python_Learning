'''
二叉查找树（英语：Binary Search Tree）
也称二叉搜索树、有序二叉树（ordered binary tree），排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：
1.若任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2.若任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3.任意节点的左、右子树也分别为二叉查找树；
4.没有键值相等的节点。
'''

'''
二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为O(log n)
二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、multiset、关联数组等。
二叉查找树的查找过程和次优二叉树类似，通常采取二叉链表作为二叉查找树的存储结构。
中序遍历二叉查找树可得到一个关键字的有序序列，一个无序序列可以通过构造一棵二叉查找树变成一个有序序列，构造树的过程即为对无序序列进行查找的过程。
每次插入的新的结点都是二叉查找树上新的叶子结点，在进行插入操作时，不必移动其它结点，只需改动某个结点的指针，由空变为非空即可。
搜索、插入、删除的复杂度等于树高，期望 O(log n)，最坏 O(n)（数列有序，树退化成线性表）。
虽然二叉查找树的最坏效率是O(n),但它支持动态查询，且有很多改进版的二叉查找树可以使树高为 O(log n),如SBT,AVL树，红黑树等。
故不失为一种好的动态查找方法。
'''

'''
在二叉查找树删除结点的算法

删除一个有左、右子树的节点
在二叉查找树删去一个结点，分三种情况讨论：
1.若*p结点为叶子结点，即PL（左子树）和PR（右子树）均为空树。由于删去叶子结点不破坏整棵树的结构，则只需修改其双亲结点的指针即可。
2.若*p结点只有左子树PL或右子树PR，此时只要令PL或PR直接成为其双亲结点*f的左子树（当*p是左子树）或右子树（当*p是右子树）即可，作此修改也不破坏二叉查找树的特性。
3.若*p结点的左子树和右子树均不空。在删去*p之后，为保持其它元素之间的相对位置不变，可按中序遍历保持有序进行调整，
可以有两种做法：其一是令*p的左子树为*f的左/右（依*p是*f的左子树还是右子树而定）子树，*s为*p左子树的最右下的结点，而*p的右子树为*s的右子树；
其二是令*p的直接前驱（in-order predecessor）或直接后继（in-order successor）替代*p，然后再从二叉查找树中删去它的直接前驱（或直接后继）。
'''
def find_min(self):   # Gets minimum node (leftmost leaf) in a subtree
    current_node = self
    while current_node.left_child:
        current_node = current_node.left_child
    return current_node

def replace_node_in_parent(self, new_value=None):
    if self.parent:
        if self == self.parent.left_child:
            self.parent.left_child = new_value
        else:
            self.parent.right_child = new_value
    if new_value:
        new_value.parent = self.parent

def binary_tree_delete(self, key):
    if key < self.key:
        self.left_child.binary_tree_delete(key)
    elif key > self.key:
        self.right_child.binary_tree_delete(key)
    else: # delete the key here
        if self.left_child and self.right_child: # if both children are present
            successor = self.right_child.find_min()
            self.key = successor.key
            successor.binary_tree_delete(successor.key)
        elif self.left_child:   # if the node has only a *left* child
            self.replace_node_in_parent(self.left_child)
        elif self.right_child:  # if the node has only a *right* child
            self.replace_node_in_parent(self.right_child)
        else: # this node has no children
            self.replace_node_in_parent(None)

'''
二叉查找树的遍历
中序遍历（in-order traversal）二叉查找树的Python代码：
'''
def traverse_binary_tree(node, callback):
    if node is None:
        return
    traverse_binary_tree(node.leftChild, callback)
    callback(node.value)
    traverse_binary_tree(node.rightChild, callback)
'''
排序（或称构造）一棵二叉查找树
用一组数值建造一棵二叉查找树的同时，也把这组数值进行了排序。其最差时间复杂度为O(n^{2})。
例如，若该组数值经是有序的（从小到大），则建造出来的二叉查找树的所有节点，都没有左子树。
自平衡二叉查找树可以克服上述缺点，其时间复杂度为O(nlog n)。
一方面，树排序的问题使得CPU Cache性能较差，特别是当节点是动态内存分配时。而堆排序的CPU Cache性能较好。
另一方面，树排序是最优的增量排序（incremental sorting）算法，保持一个数值序列的有序性。
'''
# def build_binary_tree(values):
#     tree = None
#     for v in values:
#         tree = binary_tree_insert(tree, v)
#     return tree

def get_inorder_traversal(root):
    '''
    Returns a list containing all the values in the tree, starting at *root*.
    Traverses the tree in-order(leftChild, root, rightChild).
    '''
    result = []
    traverse_binary_tree(root, lambda element: result.append(element))
    return result

'''
# 二叉查找树性能分析
每个结点的 C_i为该结点的层次数。
最坏情况下，当先后插入的关键字有序时，构成的二叉查找树蜕变为单支树，树的深度为 n，其平均查找长度为 frac {n+1}{2} （和顺序查找相同），
最好的情况是二叉查找树的形态和折半查找的判定树相同，其平均查找长度和 log_2(n)成正比O(log_2(n)。
'''