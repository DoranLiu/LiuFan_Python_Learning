'''
1.冒泡排序(bubble sort)：
每个回合都从第一个元素开始和它后面的元素比较，如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
每次遍历都将剩下的元素中最大的那个放到了序列的“最后”(除去了前面已经排好的那些元素)。注意检测是否已经完成了排序，如果已完成就可以退出了。
时间复杂度O(n^2)
'''
def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                # temp = a_list[i]
                # a_list[i] = a_list[i + 1]
                # a_list[i + 1] = temp
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1


a_list = [20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
short_bubble_sort(a_list)
print('short_bubble_sort: ',a_list)