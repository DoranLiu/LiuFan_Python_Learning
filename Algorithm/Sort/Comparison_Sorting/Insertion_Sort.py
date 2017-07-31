'''
3.插入排序(insertion sort)：

时间复杂度 O(n^2)
空间复杂度 O(1)

最好情况：O(n)

排序时间与输入有关：
    输入的元素个数；
    元素已排序的程度。

最佳情况，输入数组是已经排好序的数组，运行时间是n的线性函数；
最坏情况，输入数组是逆序，运行时间是n的二次函数。

每次假设前面的元素都是已经排好序了的，然后将当前位置的元素插入到原来的序列中，为了尽快地查找合适的插入位置，可以使用二分查找。

别误以为二分查找可以降低它的复杂度，因为插入排序还需要移动元素的操作

步骤：

从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果被扫描的元素（已排序）大于新元素，将该元素后移一位
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5

'''
from random import randrange

def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
            ary[index] = temp
    return ary

# 迭代的方式
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

# 使用二分查找的插入排序
def insertion_sort_binarysearch(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        low=0
        high=index-1
        while low<=high:
            mid=(low+high)/2
            if a_list[mid]>current_value:
                high=mid-1
            else:
                low=mid+1
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position -1
        a_list[position] = current_value

# 递归版本的插入排序，但list的size不能过大，否则会栈溢出。
def insertion_sort_rec(seq, i):
    if i == 0: return  # Base case -- do nothing
    insertion_sort_rec(seq, i - 1)  # Sort 0..i-1
    j = i  # Start "walking" down
    while j > 0 and seq[j - 1] > seq[j]:  # Look for OK spot
        seq[j - 1], seq[j] = seq[j], seq[j - 1]  # Keep moving seq[j] down
        j -= 1  # Decrement j



a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print('insertion: ',a_list)
insertion_sort_binarysearch(a_list)
print('insertion_binary: ',a_list)

a_list = [randrange(1000) for i in range(100)]
ins_sort_rec(a_list, len(a_list)-1)