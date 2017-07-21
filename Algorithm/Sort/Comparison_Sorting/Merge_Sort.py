'''
4.合并(归并)排序(merge sort)：

时间复杂度 O(NlogN)
空间复杂度 O(N+logN)
排序时间与输入无关，最佳情况，最坏情况都是如此, 稳定。

原理：
可以将数组分成二组。
依次类推，当分出来的小组只有一个数据时，可以认为这个小组组内已经达到了有序，然后再合并相邻的二个小组就可以了。
这样通过先递归的分解数列，再合并数列就完成了归并排序.这是典型的分治法策略。

先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。
然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。
如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。然后合并排序相邻二个小组即可。

复杂度：
归并排序的时间复杂度，合并耗费 O(n) 时间，而由完全二叉树的深度可知，整个归并排序需要进行log_2n次，因此，总的时间复杂度为 O(nlogn)，而且这是归并排序算法中最好、最坏、平均的时间性能。
由于归并排序在归并过程中需要与原始记录序列同样数量的存储空间存放归并结果 以及 递归时深度为 log_2n 的栈空间，因此空间复杂度为O(n+logn)。

稳定性：
对代码进行仔细研究，发现 Merge 函数中有if (L[i]<R[j]) 语句，这就说明它需要两两比较，不存在跳跃，因此归并排序是一种稳定的排序算法。

总结：
归并排序是一种比较占用内存，但却效率高且稳定的算法。
'''
def merge_sort(a_list):
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i=i+1
            else:
                a_list[k] = right_half[j]
                j=j+1
            k=k+1
        while i < len(left_half):
            a_list[k] = left_half[i]
            i=i+1
            k=k+1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j=j+1
            k=k+1
    print("Merging ", a_list)

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)

#   #

def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组
def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

'''
归并排序
时间复杂度为 O(NlogN)
'''
def mergesort(seq):
    mid = len(seq)//2
    left,right = seq[:mid],seq[mid:]
    if len(left) > 1: left = mergesort(left)
    if len(right) > 1: right = mergesort(right)
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res
