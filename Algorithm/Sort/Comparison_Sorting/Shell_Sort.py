'''
6.希尔排序：
希尔排序，也称递减增量排序算法，实质是分组插入排序。

类似合并排序和插入排序的结合体，二路合并排序将原来的数组分成左右两部分，
希尔排序则将数组按照一定的间隔分成几部分，每部分采用插入排序来排序，有意思的是这样做了之后，
元素很多情况下就差不多在它应该呆的位置，所以效率不一定比插入排序差。
时间复杂度 [O(n),O(n^2)]
空间复杂度 O(1)

不稳定

希尔排序的基本思想是：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

例如，假设有这样一组数[ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]，如果我们以步长为5开始进行排序，我们可以通过将这列表放在有5列的表中来更好地描述算法，这样他们就应该看起来是这样：

13 14 94 33 82
25 59 94 65 23
45 27 73 25 39
10
然后我们对每列进行排序：

10 14 73 25 23
13 27 94 33 39
25 59 94 65 82
45
将上述四行数字，依序接在一起时我们得到：[ 10 14 73 25 23 13 27 94 33 39 25 59 94 65 82 45 ]。这时10已经移至正确位置了，然后再以3为步长进行排序：

10 14 73
25 23 13
27 94 33
39 25 59
94 65 82
45
排序之后变为：

10 14 13
25 23 33
27 25 59
39 65 73
45 94 82
94
最后以1步长进行排序（此时就是简单的插入排序了）。
'''


def shell_sort(a_list):
    #how many sublists, also how many elements in a sublist
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

# 取步长
def gap_insertion_sort(a_list, start, gap):
    #start+gap is the second element in this sublist
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap] #move backward
            position = position - gap
            a_list[position] = current_value


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20, 88]
shell_sort(a_list)
print(a_list)

# 源码的步长的选择是从 n/2 开始，每次再减半，直至为0。步长的选择直接决定了希尔排序的复杂度。在维基百科上有对于步长串行的详细介绍。
def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary
