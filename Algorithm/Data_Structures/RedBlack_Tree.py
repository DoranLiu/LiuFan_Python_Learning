'''
红黑树和AVL树一样都对插入时间、删除时间和查找时间提供了最好可能的最坏情况担保。
这不只是使它们在时间敏感的应用如实时应用（real time application）中有价值，而且使它们有在提供最坏情况担保的其他数据结构中作为建造板块的价值；

例如，在计算几何中使用的很多数据结构都可以基于红黑树。
红黑树在函数式编程中也特别有用，在这里它们是最常用的持久数据结构（persistent data structure）之一，
它们用来构造关联数组和集合，每次插入、删除之后它们能保持为以前的版本。除了O(log n)的时间之外，红黑树的持久版本对每次插入或删除需要O(log n)的空间。
红黑树是2-3-4树的一种等同:
换句话说，对于每个2-3-4树，都存在至少一个数据元素是同样次序的红黑树。
在2-3-4树上的插入和删除操作也等同于在红黑树中颜色翻转和旋转。这使得2-3-4树成为理解红黑树背后的逻辑的重要工具，这也是很多介绍算法的教科书在红黑树之前介绍2-3-4树的原因，尽管2-3-4树在实践中不经常使用。
红黑树相对于AVL树来说，牺牲了部分平衡性以换取插入/删除操作时少量的旋转操作，整体来说性能要优于AVL树。
'''

'''
性质
红黑树是每个节点都带有颜色属性的二叉查找树，颜色为红色或黑色。
在二叉查找树强制一般要求以外，对于任何有效的红黑树我们增加了如下的额外要求：
1.节点是红色或黑色。
2.根是黑色。
3.所有叶子都是黑色（叶子是NIL节点）。
4.每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
5.从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。
'''

class RBTree:
    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode:
    def __init__(self, x):
        self.key = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'

class Solution:
    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            if x.key != 0:
                print('key:', x.key, 'parent:', x.parent.key, 'color:', x.color)
            self.InorderTreeWalk(x.right)

    def LeftRotate(self, T, x):
        y = x.right
        x.right = y.left
        if y.left != T.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right
        if y.right != T.nil:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == T.nil:
            T.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def RBInsert(self, T, z):
        # init z
        z.left = T.nil
        z.right = T.nil
        z.parent = T.nil

        y = T.nil
        x = T.root
        while x != T.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == T.nil:
            T.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.left = T.nil
        z.right = T.nil
        z.color = 'red'
        self.RBInsertFixup(T,z)

    def RBInsertFixup(self, T, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.LeftRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.RightRotate(T,z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.RightRotate(T, z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.LeftRotate(T, z.parent.parent)
        T.root.color = 'black'

    def RBTransplant(self, T, u, v):
        if u.parent == T.nil:
            T.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBDelete(self, T, z):
        y = z
        y_original_color = y.color
        if z.left == T.nil:
            x = z.right
            self.RBTransplant(T, z, z.right)
        elif z.right == T.nil:
            x = z.left
            self.RBTransplant(T, z, z.left)
        else:
            y = self.TreeMinimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RBTransplant(T, y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RBTransplant(T, z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.RBDeleteFixup(T, x)

    def RBDeleteFixup(self, T, x):
        while x != T.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.LeftRotate(T, x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.RightRotate(T, w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.LeftRotate(T, x.parent)
                    x = T.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.RightRotate(T, x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.LeftRotate(T, w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.RightRotate(T, x.parent)
                    x = T.root
        x.color = 'black'

    def TreeMinimum(self, x):
        while x.left != T.nil:
            x = x.left
        return x

nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
s = Solution()
for node in nodes:
    s.RBInsert(T,RBTreeNode(node))

s.InorderTreeWalk(T.root)

s.RBDelete(T,T.root)
print('after delete')
s.InorderTreeWalk(T.root)