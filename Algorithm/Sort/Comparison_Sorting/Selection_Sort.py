'''
2.选择排序(selection sort)：

时间复杂度 O(n^2)
空间复杂度 O(1)

排序时间与输入无关，最佳情况，最坏情况都是如此, 不稳定

每个回合都选择出剩下的元素中最大的那个，选择的方法是首先默认第一元素是最大的，如果后面的元素比它大的话，那就更新剩下的最大的元素值，
找到剩下元素中最大的之后将它放入到合适的位置就行了。和冒泡排序类似，只是找剩下的元素中最大的方式不同而已。
'''
# 迭代版的选择排序
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1, 0, -1): # range（start，end，scan) 倒序输出
        pos_of_max = 0  # 首先默认第一个元素是最大的
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        # temp = a_list[fill_slot]
        # a_list[fill_slot] = a_list[pos_of_max]
        # a_list[pos_of_max] = temp
        a_list[fill_slot],a_list[pos_of_max]=a_list[pos_of_max],a_list[fill_slot]

def selection_sort2(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary


# 递归版的选择排序
def selection_sort_rec(seq, i):
    if i == 0: return  # Base case -- do nothing
    max_j = i  # Idx. of largest value so far
    for j in range(i):  # Look for a larger value
        if seq[j] > seq[max_j]: max_j = j  # Found one? Update max_j
    seq[i], seq[max_j] = seq[max_j], seq[i]  # Switch largest into place
    selection_sort_rec(seq, i - 1)  # Sort 0..i-1

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 11]
selection_sort(a_list)
print('selection_sort: ',a_list)

selection_sort_rec(a_list,len(a_list)-1)
print('selection_sort_rec: ',a_list)
