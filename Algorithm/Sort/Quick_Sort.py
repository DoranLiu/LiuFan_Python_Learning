'''
5.快速排序(quick sort)：

想法一：它选择第一个元素作为主元，它同样可以按照下面提到的算法导论中将数组分成了4个不同的部分，但是这里其实有更好的解释方法。
首先，它每次都是选择第一个元素都为主元，这个回合就是要确定主元的位置；
然后，有两个指针，一个leftmark指向主元的后面一个位置，另一个rightmark指向要排序的数组最后一个元素；
接着，两个指针分别向中间移动，leftmark遇到比主元大的元素停止，rightmark遇到比主元小的元素停止，
如果此时leftmark<rightmark，也就是说中间还有未处理(未确定与主元大小关系)的元素，那么就交换leftmark和rightmark位置上的元素，
然后重复刚才的移动操作，直到rightmark<leftmark；
最后，停止移动时候rightmark就是主元要放置的位置，因为它停在一个比主元小的元素的位置上，之后交换主元和rightmark指向的元素即可。
完了之后，递归地对主元左右两边的数组进行排序即可。
'''
def quick_sort_1(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition_1(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)

def partition_1(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_1(a_list)
print(a_list)


'''
想法二：如下图所示(摘自算法导论)，它选择最后的那个元素作为主元，它的思路是将数组划分成4部分：

第一部分：$p \le k \le i, A[k] \le pivot$
第二部分：$i+1 \le k \le j-1, A[k] \gt pivot$
第三部分：$j \le k \le r-1, A[k]$可以取任何值(因为它们还没有进行处理)
第四部分：$p \le k \le i, A[k] = pivot$

首先，让i指向要排序的数组的第一个元素的前面，p和j都指向第一个元素；
然后，一直移动j直到主元前一个位置，一旦发现一个小于主元的元素就让i指向它的下一个位置，然后交换i和j对应位置上的元素。
这样一定是可行的，因为i一直都是指向已发现的小于主元的元素中的最后一个，从i+1开始就大于主元了(或者还未确定/未处理)，
而j一直都是指向大于主元的元素中最后一个的后面一个位置，所以i+1和j位置上的元素交换就可以使得j发现的这个小于主元的元素移动到第一部分，
而i+1位置上大于主元的元素移动到j的位置上，即第二部分的最后一个位置上。
'''
def partition_2(a,low,high):
    key = a[high] # pivot
    i = low - 1 # temp
    for j in range(low,high):
        if a[j] < key:
            i +=1
            a[j],a[i] = a[i],a[j]

    a[high],a[i+1] = a[i+1],a[high] # i+1 is the split point
    return  i+1

# quick sort
def quick_sort2(a,low,high):
    if low < high:
        p = partition_2(a,low,high)
        quick_sort2(a, low, p-1)
        quick_sort2(a, p+1, high)

# print array
def print_array(a,leng):
    for i in range(leng):
        print(a[i])
        print('\n')

a=[3,5,2,7,9,10,33,28,19,6,8]
quick_sort2(a, 0, 10)
print_array(a,11)

# 由于快排每次都能够确定一个元素在数组中最终的位置，所以可以用快排来解决很多变种问题，
# 例如在线性时间内求中位数或者其他顺序统计量的问题(例如第k大或者第k小的元素)

# 关于快排的性能分析,一般来说划分之后两边越均衡的话快排的性能更好。为了避免最坏的情况出现(原始的数组是已经是有序的)可以使用随机化版本的快排。
# 另外，为了减少快排调用的栈深度可以使用模拟尾递归技术，通过对快排的修改可以保证最坏情况下栈深度为O(nlgn)，该内容可以参见算法导论习题7-4。



