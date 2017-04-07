'''
1.冒泡排序(bubble sort)：

时间复杂度 O(n^2)
空间复杂度 O(1)

排序时间与输入无关，最好，最差，平均都是O(n^2)
稳定，因为存在两两比较，不存在跳跃。

原理：
每个回合都从第一个元素开始和它后面的元素比较，如果比它后面的元素更大的话就交换，一直重复，直到这个元素到了它能到达的位置。
每次遍历都将剩下的元素中最大的那个放到了序列的“最后”(除去了前面已经排好的那些元素)。注意检测是否已经完成了排序，如果已完成就可以退出了。

缺陷：
在排序过程中，执行完当前的第i趟排序后，可能数据已全部排序完备，但是程序无法判断是否完成排序，会继续执行剩下的(n-1-i)趟排序。
解决方法：
设置一个flag位, 如果一趟无元素交换，则 flag = 0; 以后再也不进入第二层循环。
当排序的数据比较多时排序的时间会明显延长，因为会比较 n*(n-1)/2次。
'''

def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i],a_list[i+1] = a_list[i+1], a_list[i]
        pass_num = pass_num - 1


a_list = [20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
short_bubble_sort(a_list)
print('short_bubble_sort: ',a_list)


def bubble_sort(ary):
    n = len(ary)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  ary[j-1] > ary[j] :       #如果前者比后者大
                ary[j-1],ary[j] = ary[j],ary[j-1]       #则交换两者
    return ary


#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1,n-i):
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                flag = 0
        if flag :                   #全排好序了，直接跳出
            break
    return ary

#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return ary