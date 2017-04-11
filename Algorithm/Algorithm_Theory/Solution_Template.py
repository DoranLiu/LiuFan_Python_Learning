'''
解题思路模板：

这个模版的核心是， 将binary search 问题转化成：
寻找第一个或者最后一个，该target元素出现的位置的问题，Find the any/first/last position of target in nums.

start + 1 < end 表示， 当指针指到两个元素，相邻或者相交的时候， 循环停止。
这样的话在最终分情况讨论的时候，只用考虑1～2个元素。
start + (end - start) / 2 写C++ 和 Java的同学要考虑到int overflow的问题， 所以需要考虑边界情况。
A[mid] ==, >, < 在循环中， 分三种情况讨论边界。
要注意， 在移动start和end的时候， 只要单纯的把指针指向mid的位置， 不要+1或者-1。
因为只移动边界到mid的位置， 不会误删除target。
在工程中，尽量在程序最后的时候统一写return, 这样可以增强可读性。
A[start], A[end]? target 在循环结束时，因为只有1～2个元素需要讨论，所以结果非常容易解释清楚。

只存在的2种情况为：
    1. start + 1 == end 边界指向相邻的两个元素， 这时只需要分情况讨论start和end与target的关系，就可以得出结果。
    2. start == end 边界指向同一元素， 其实这个情况还是可以按照1的方法，分成start``end讨论，只不过讨论结果一样而已。
'''

class Solution_Binary:
    def binary_search(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end: # 当指针指到两个元素，相邻或者相交的时候，循环停止
            mid = int((start + end) / 2)
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        if array[start] == target:
            return start
        if array[end] == target:
            return end
        return -1

arr = [5,6,7,8,8,9,10]
tar = 8

solu = Solution_Binary()
print(solu.binary_search(arr,tar))

'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=Search for a Range=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# Search for a Range

# 给出[5, 7, 7, 8, 8, 10]和目标值target=8,
# 返回[3, 4]

class Solution_Search:
    def search_range(self, array, target):
        ret = [-1, -1]
        if not array:
            return ret
        # search first position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = int((st + ed) / 2)
            if array[mid] == target:
                ed = mid
            elif array[mid] < target:
                st = mid
            else:
                ed = mid
        if array[st] == target:
            ret[0] = st
        elif array[ed] == target:
            ret[0] = ed

        # search last position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = int((st + ed) / 2)
            if array[mid] == target:
                st = mid
            elif array[mid] < target:
                st = mid
            else:
                ed= mid
        if array[ed] == target:
            ret[1] = ed
        elif array[st] == target:
            ret[1] = st

        return ret
# 源码分析
# search range的问题可以理解为， 寻找第一次target出现的位置和最后一次target出现的位置。
# 当寻找第一次target出现位置的循环中， array[mid] == target表示， target可以出现在mid或者mid更前的位置， 所以将ed移动到mid。
# 当循环跳出时， st的位置在ed之前，所以先判断在st位置上是否是target， 再判断ed位置。
# 当寻找最后一次target出现位置的循环中，array[mid] == target表示， target可以出现在mid或者mid之后的位置， 所以将st移动到mid。
# 当循环结束时，ed的位置比st的位置更靠后， 所以先判断ed的位置是否为target， 再判断st位置。 最后返回ret。

solus = Solution_Search()
print(solus.search_range(arr,tar))