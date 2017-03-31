'''
3.插入排序(insertion sort)：
每次假设前面的元素都是已经排好序了的，然后将当前位置的元素插入到原来的序列中，为了尽快地查找合适的插入位置，可以使用二分查找。
时间复杂度O(n^2)
别误以为二分查找可以降低它的复杂度，因为插入排序还需要移动元素的操作
'''
def insertion_sort(a_list):
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

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


a_list = [54, 26, 93, 15, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print('insertion: ',a_list)
insertion_sort_binarysearch(a_list)
print('insertion_binary: ',a_list)
