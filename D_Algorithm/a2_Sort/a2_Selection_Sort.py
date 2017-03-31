'''
2.选择排序(selection sort)：
每个回合都选择出剩下的元素中最大的那个，选择的方法是首先默认第一元素是最大的，如果后面的元素比它大的话，那就更新剩下的最大的元素值，
找到剩下元素中最大的之后将它放入到合适的位置就行了。和冒泡排序类似，只是找剩下的元素中最大的方式不同而已。
时间复杂度O(n^2)
'''
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


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 11]
selection_sort(a_list)
print('selection_sort: ',a_list)
