'''
堆排序

性能分析:
时间复杂度 O(nlogn)
空间复杂度 O(1).
从这一点就可以看出，堆排序在时间上类似归并，但是它又是一种原地排序，空间复杂度小于归并的O(n+logn)

排序时间与输入无关，最好，最差，平均都是O(nlogn). 不稳定

原理：
堆排序借助了堆这个数据结构，堆类似二叉树，又具有堆积的性质（子节点的关键值总小于（大于）父节点） 堆排序包括两个主要操作:
    1。保持堆的性质heapify(A,i)，时间复杂度 O(logn)
    2。建堆 buildmaxheap(A)，时间复杂度 O(n) 线性时间建堆

二叉堆具有以下性质：
    1。父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
    2。每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。

步骤：
    1。构造最大堆（Build_Max_Heap）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
    2。堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
    3.最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点 。

对于大数据的处理：
如果对100亿条数据选择Topk数据，选择快速排序好还是堆排序好？
答案是只能用堆排序。
堆排序只需要维护一个k大小的空间，即在内存开辟k大小的空间。而快速排序需要开辟能存储100亿条数据的空间，which is impossible.

应用：
堆这种数据结构的很好的应用是 优先级队列，如作业调度。
'''

def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

a = heap_sort([3, 1, 4, 9, 6, 7, 5, 8, 2, 10])
print(a)

