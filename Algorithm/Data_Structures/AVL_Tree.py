'''
AVL树：
在计算机科学中，AVL树是最先发明的自平衡二叉查找树。
在AVL树中任何节点的两个子树的高度最大差别为一，所以它也被称为高度平衡树。
查找、插入和删除在平均和最坏情况下都是 O(log n)。
增加和删除可能需要通过一次或多次树旋转来重新平衡这个树。
AVL树得名于它的发明者G.M. Adelson-Velsky和E.M. Landis，他们在1962年的论文《An algorithm for the organization of information》中发表了它。
节点的平衡因子是它的左子树的高度减去它的右子树的高度（有时相反）。带有平衡因子1、0或 -1的节点被认为是平衡的。
带有平衡因子-2或2的节点被认为是不平衡的，并需要重新平衡这个树。平衡因子可以直接存储在每个节点中，或从可能存储在节点中的子树高度计算出来。
'''
'''
实现描述：
假设平衡因子是左子树的高度减去右子树的高度所得到的值，又假设由于在二叉排序树上插入节点而失去平衡的最小子树根节点的指针为a（即a是离插入点最近，且平衡因子绝对值超过1的祖先节点），

则失去平衡后进行的规律可归纳为下列四种情况：
单向右旋平衡处理LL：由于在*a的左子树根节点的左子树上插入节点，*a的平衡因子由1增至2，致使以*a为根的子树失去平衡，则需进行一次右旋转操作；
单向左旋平衡处理RR：由于在*a的右子树根节点的右子树上插入节点，*a的平衡因子由-1变为-2，致使以*a为根的子树失去平衡，则需进行一次左旋转操作；
双向旋转（先左后右）平衡处理LR：由于在*a的左子树根节点的右子树上插入节点，*a的平衡因子由1增至2，致使以*a为根的子树失去平衡，则需进行两次旋转（先左旋后右旋）操作。
双向旋转（先右后左）平衡处理RL：由于在*a的右子树根节点的左子树上插入节点，*a的平衡因子由-1变为-2，致使以*a为根的子树失去平衡，则需进行两次旋转（先右旋后左旋）操作。

在平衡的二叉排序树BBST (Balancing Binary Search Tree)上插入一个新的数据元素e的递归算法可描述如下：
若BBST为空树，则插入一个数据元素为e的新节点作为BBST的根节点，树的深度增1；
若e的关键字和BBST的根节点的关键字相等，则不进行；
若e的关键字小于BBST的根节点的关键字，而且在BBST的左子树中不存在和e有相同关键字的节点，则将e插入在BBST的左子树上，并且当插入之后的左子树深度增加（+1）时，分别就下列不同情况处理之：
BBST的根节点的平衡因子为-1（右子树的深度大于左子树的深度，则将根节点的平衡因子更改为0，BBST的深度不变；
BBST的根节点的平衡因子为0（左、右子树的深度相等）：则将根节点的平衡因子更改为1，BBST的深度增1；
BBST的根节点的平衡因子为1（左子树的深度大于右子树的深度）：则若BBST的左子树根节点的平衡因子为1：则需进行单向右旋平衡处理，并且在右旋处理之后，将根节点和其右子树根节点的平衡因子更改为0，树的深度不变；
若e的关键字大于BBST的根节点的关键字，而且在BBST的右子树中不存在和e有相同关键字的节点，则将e插入在BBST的右子树上，并且当插入之后的右子树深度增加（+1）时，分别就不同情况处理之。

'''
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None,balanceFactor=0):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent
        self.balanceFactor=balanceFactor; #default new node balance factor is 0

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def inorder(self,node):
        if node.leftChild:
            self.inorder(node.leftChild)
        self.print_node(node)
        if node.rightChild:
            self.inorder(node.rightChild)

    def levelorder(self,node):
        nodes = []
        nodes.append(node)
        while len(nodes)>0:
            current_node = nodes.pop(0)
            self.print_node(current_node)
            if current_node.leftChild:
                nodes.append(current_node.leftChild)
            if current_node.rightChild:
                nodes.append(current_node.rightChild)

    def print_node(self,node):
        if node.parent:
            print([node.key,node.payload,node.parent.key])
        else:
            print([node.key,node.payload])

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self,key):
        return self.get(key)

    def __contains__(self,key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
        self.delete(key)

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    def remove(self,currentNode):
        if currentNode.isLeaf(): #leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren(): #interior
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        else: # this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


class AVLTree(BinarySearchTree):

    # def put(self,key,val):
    #     if self.root:
    #         self._put(key,val,self.root)
    #     else:
    #         self.root = TreeNode(key,val)
    #         self.root.balanceFactor = 0
    #     self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self,rotRoot): #rotate left
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild != None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot): #rotate right
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild # deal child
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot #deal child parent
        newRoot.parent = rotRoot.parent #deal root parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.rightChild = rotRoot #deal new root right child
        rotRoot.parent = newRoot #deal old root parent
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self,node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

#test code
# test avl tree
print('test avl')
mytree = AVLTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
mytree[5]='dog'
mytree[1]='cat'
mytree.levelorder(mytree.root)

# test bst
print('test bst')
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
mytree[5]='dog'
mytree[1]='cat'
mytree.levelorder(mytree.root)

# test avl
# [4, 'blue']
# [2, 'at', 4]
# [6, 'yellow', 4]
# [1, 'cat', 2]
# [3, 'red', 2]
# [5, 'dog', 6]
# test bst
# [3, 'red']
# [2, 'at', 3]
# [4, 'blue', 3]
# [1, 'cat', 2]
# [6, 'yellow', 4]
# [5, 'dog', 6]