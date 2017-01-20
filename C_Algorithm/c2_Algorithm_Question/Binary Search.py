#Binary Search - 二分查找
#本章主要总结二分搜索相关的题。

#    能使用二分搜索的前提是数组已排序。
#    二分查找的使用场景：（1）可转换为find the first/last position of...（2）时间复杂度至少为O(lgn)。
#    递归和迭代的使用场景：能用迭代就用迭代，特别复杂时采用递归。

'''
Question

Search Insert Position:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
问题可以转化为， 寻找first position that value is >= target。如果没找到， 那么就插入在list的尾部。
You may assume NO duplicates in the array.
Example:
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''
def searchInsert(A, target):
    if not A:
        return 0
    st, ed = 0, len(A) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if A[mid] == target:
            ed = mid
        elif A[mid] < target:
            st = mid
        else:
            ed = mid
    if A[st] >= target:
        return st
    elif A[ed] >= target:
        return ed
    else:
        return len(A)

#源码分析:
#分析三种典型情况：
#    目标值在数组范围之内，最后返回值一定是start + 1
#    目标值比数组最小值还小，此时start 一直为-1, 故最后返回start + 1 也没错，也可以将-1 理解为数组前一个更小的值
#    目标值大于等于数组最后一个值，由于循环退出条件为start + 1 == end, 那么循环退出时一定有start = A.length - 1, 应该返回start + 1
#综上所述，返回start + 1是非常优雅的实现。其实以上三种情况都可以统一为一种方式来理解，即索引-1 对应于在数组前方插入一个非常小的数，索引end 即对应数组后方插入一个非常大的数，那么要插入的数就一定在start 和end 之间了。
#有时复杂的边界条件处理可以通过『补项』这种优雅的方式巧妙处理。

#复杂度分析
# 时间复杂度 O(logn), 空间复杂度 O(1).
'''
Question:

Search for a Range:
Given a sorted array of n integers, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].
Example:
Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4].
'''
def searchRange(self, A, target):
    ret = [-1, -1]
    if not A:
        return ret

    # find the first position of target
    st, ed = 0, len(A) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if A[mid] == target:
            ed = mid
        elif A[mid] < target:
            st = mid
        else:
            ed = mid
    if A[st] == target:
        ret[0] = st
    elif A[ed] == target:
        ret[0] = ed
    # find the last position of target
    st, ed = 0, len(A) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if A[mid] == target:
            st = mid
        elif A[mid] < target:
            st = mid
        else:
            ed = mid
    if A[ed] == target:
        ret[1] = ed
    elif A[st] == target:
        ret[1] = st

    return ret

#源码分析
#    首先对输入做异常处理，数组为空或者长度为0
#    分 lower/upper bound 两次搜索，注意如果在 lower bound 阶段未找到目标值时，upper bound 也一定找不到。
#    取A[lb + 1] 时一定要注意判断索引是否越界！

#复杂度分析
#两次二分搜索，时间复杂度仍为 O(logn).

'''
Question

First Bad Version:
The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.

You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

Example:
Given n = 5:
isBadVersion(3) -> false
isBadVersion(5) -> true
isBadVersion(4) -> true

Here we are 100% sure that the 4th version is the first bad version.
'''

def findFirstBadVersion(self, n):
    lb, ub = 0, n + 1
    while lb + 1 < ub:
        mid = lb + (ub - lb) / 2
        if VersionControl.isBadVersion(mid):
            ub = mid
        else:
            lb = mid

    return lb + 1

#源码分析:
#lower bound 的实现，这里稍微注意下lb 初始化为 0，因为 n 从1开始。ub 和 lb 分别都在什么条件下更新就好了。另外这里并未考虑 n <= 0 的情况。
#复杂度分析
#二分搜索，O(logn).

'''
Question

Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example:
Consider the following matrix:
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''

#O(log(n) + log(m)) time
#题解 - 一次二分搜索 V.S. 两次二分搜索
#    一次二分搜索 - 由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。时间复杂度为 O(log(mn))=O(log(m)+log(n))O(log(mn))=O(log(m)+log(n))O(log(mn))=O(log(m)+log(n))
#    两次二分搜索 - 先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。

#一次二分搜索
def search_matrix(matrix, target):
    # Find the first position of target
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    st, ed = 0, m * n - 1

    while st + 1 < ed:
        mid = (st + ed) / 2
        if matrix[mid / n][mid % n] == target:
            return True
        elif matrix[mid / n][mid % n] < target:
            st = mid
        else:
            ed = mid
    return matrix[st / n][st % n] == target or \
            matrix[ed / n][ed % n] == target

#源码分析:
#仍然可以使用经典的二分搜索模板(lower bound)，注意下标的赋值即可。
#    首先对输入做异常处理，不仅要考虑到matrix为null，还要考虑到matrix[0]的长度也为0。
#    由于 lb 的变化处一定小于 target, 故在 else 中判断。

#复杂度分析
#二分搜索，O(logmn)O(\log mn)O(logmn).

#两次二分法
def search_matrix(self, matrix, target):
    if not matrix or not matrix[0]:
        return False

    # first pos >= target
    st, ed = 0, len(matrix) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if matrix[mid][-1] == target:
            st = mid
        elif matrix[mid][-1] < target:
            st = mid
        else:
            ed = mid
    if matrix[st][-1] >= target:
        row = matrix[st]
    elif matrix[ed][-1] >= target:
        row = matrix[ed]
    else:
        return False

    # binary search in row
    st, ed = 0, len(row) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            st = mid
        else:
            ed = mid
    return row[st] == target or row[ed] == target

#源码分析
#    先找到first position的行， 这一行的最后一个元素大于等于target
#    再在这一行中找target

#复杂度分析
#二分搜索， O(logm+logn)O(\log m + \log n)O(logm+logn)

'''
Question

Search a 2D Matrix:
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example:
Consider the following matrix:
[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
Given target = 3, return true.
'''

#O(log(n) + log(m)) time
#题解 - 一次二分搜索 V.S. 两次二分搜索
#    一次二分搜索 - 由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。时间复杂度为 O(log(mn))=O(log(m)+log(n))O(log(mn))=O(log(m)+log(n))O(log(mn))=O(log(m)+log(n))
#    两次二分搜索 - 先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。

#一次二分搜索
def search_matrix(self, matrix, target):
    # Find the first position of target
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    st, ed = 0, m * n - 1

    while st + 1 < ed:
        mid = (st + ed) / 2
        if matrix[mid / n][mid % n] == target:
            return True
        elif matrix[mid / n][mid % n] < target:
            st = mid
        else:
            ed = mid
    return matrix[st / n][st % n] == target or \
            matrix[ed / n][ed % n] == target

#源码分析:
#仍然可以使用经典的二分搜索模板(lower bound)，注意下标的赋值即可。
#    首先对输入做异常处理，不仅要考虑到matrix为null，还要考虑到matrix[0]的长度也为0。
#    由于 lb 的变化处一定小于 target, 故在 else 中判断。

#复杂度分析
#二分搜索，O(logmn)O(\log mn)O(logmn).

#两次二分法
def search_matrix(self, matrix, target):
    if not matrix or not matrix[0]:
        return False

    # first pos >= target
    st, ed = 0, len(matrix) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if matrix[mid][-1] == target:
            st = mid
        elif matrix[mid][-1] < target:
            st = mid
        else:
            ed = mid
    if matrix[st][-1] >= target:
        row = matrix[st]
    elif matrix[ed][-1] >= target:
        row = matrix[ed]
    else:
        return False

    # binary search in row
    st, ed = 0, len(row) - 1
    while st + 1 < ed:
        mid = (st + ed) / 2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            st = mid
        else:
            ed = mid
    return row[st] == target or row[ed] == target

#源码分析
#    先找到first position的行， 这一行的最后一个元素大于等于target
#    再在这一行中找target

#复杂度分析:
#二分搜索， O(logm+logn)O(\log m + \log n)O(logm+logn)


'''
Question
Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
Note:

Your solution should be in logarithmic complexity.
Credits:

Special thanks to @ts for adding this problem and creating all test cases.
题解1

由时间复杂度的暗示可知应使用二分搜索。首先分析若使用传统的二分搜索，若A[mid] > A[mid - 1] && A[mid] < A[mid + 1]，则找到一个peak为A[mid]；若A[mid - 1] > A[mid]，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足A[0] > A[1] > ... > A[mid -1] > A[mid]，与已知A[0] < A[1]矛盾，证毕。同理可得若A[mid + 1] > A[mid]，则A[mid]右侧必定存在一个peak。如此迭代即可得解。 由于题中假设端点外侧的值均为负无穷大，即num[-1] < num[0] && num[n-1] > num[n], 那么问题来了，这样一来就不能确定峰值一定存在了，因为给定数组为单调序列的话就咩有峰值了，但是实际情况是——题中有负无穷的假设，也就是说在单调序列的情况下，峰值为数组首部或者尾部元素，谁大就是谁了。

备注：如果本题是找 first/last peak，就不能用二分法了。
'''
def findPeak(self, A):
    if not A:
        return -1

    l, r = 0, len(A) - 1
    while l + 1 < r:
        mid = l + (r - l) / 2
        if A[mid] < A[mid - 1]:
            r = mid
        elif A[mid] < A[mid + 1]:
            l = mid
        else:
            return mid
    mid = l if A[l] > A[r] else r
    return mid

#源码分析:
#典型的二分法模板应用，需要注意的是需要考虑单调序列的特殊情况。当然也可使用紧凑一点的实现如改写循环条件为l < r，这样就不用考虑单调序列了，见实现2.

#复杂度分析
#二分法，时间复杂度 O(logn)O(\log n)O(logn).


'''
Question

Median of two Sorted Arrays:
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays.

Example
Given A=[1,2,3,4,5,6] and B=[2,3,4,5], the median is 3.5.
Given A=[1,2,3] and B=[4,5], the median is 3.
'''

#题解1 - 归并排序
#何谓"Median"? 由题目意思可得即为两个数组中一半数据比它大，另一半数据比它小的那个数。详见 中位数 - 维基百科，自由的百科全书。简单粗暴的方法就是使用归并排序的思想，挨个比较两个数组的值，取小的，最后分奇偶长度返回平均值或者中位值。

def findMedianSortedArrays(self, A, B):
    n = len(A) + len(B)
    if n % 2 == 1:
        return self.findKth(A, B, n / 2 + 1)
    else:
        smaller = self.findKth(A, B, n / 2)
        bigger = self.findKth(A, B, n / 2 + 1)
        return (smaller + bigger) / 2.0

def findKth(self, A, B, k):
    if len(A) == 0:
        return B[k - 1]
    if len(B) == 0:
        return A[k - 1]
    if k == 1:
        return min(A[0], B[0])
    
    a = A[k / 2 - 1] if len(A) >= k / 2 else None
    b = B[k / 2 - 1] if len(B) >= k / 2 else None
    
    if b is None or (a is not None and a < b):
        return self.findKth(A[k / 2:], B, k - k / 2)
    return self.findKth(A, B[k / 2:], k - k / 2)   

#源码分析
#本题用非递归的方法非常麻烦，递归的方法减少了很多边界的判断。此题的边界条件较多，不容易直接从代码看清思路。首先分析找k大的辅助程序。以 Java 的代码为例。
#    首先在主程序中排除 A, B 均为空的情况。
#    排除 A 或者 B 中有一个为空或者长度为0的情况。如果A_start > A.size() - 1，意味着A中无数提供，故仅能从B中取，所以只能是B从B_start开始的第k个数。下面的B...分析方法类似。
#    k为1时，无需再递归调用，直接返回较小值。如果 k 为1不返回将导致后面的无限循环。
#    以A为例，取出自A_start开始的第k / 2个数，若下标A_start + k / 2 - 1 < A.size()，则可取此下标对应的元素，否则置为int的最大值，便于后面进行比较，免去了诸多边界条件的判断。
#    比较A_key > B_key，取小的折半递归调用findKth。

#接下来分析findMedianSortedArrays：
#    首先考虑异常情况，A, B都为空。
#    A+B 的长度为偶数时返回len / 2和 len / 2 + 1的均值，为奇数时则返回len / 2 + 1

#复杂度分析
#找中位数，K 为数组长度和的一半，故总的时间复杂度为 O(log(m+n)).

'''
Question
Sqrt x
'''
#题解 - 二分搜索
#由于只需要求整数部分，故对于任意正整数 xxx, 设其整数部分为 kkk, 显然有 1≤k≤x1 \leq k \leq x1≤k≤x, 求解 kkk 的值也就转化为了在有序数组中查找满足某种约束条件的元素，显然二分搜索是解决此类问题的良方。
def mySqrt(self, x):
    if x < 0:
        return -1
    elif x == 0:
        return 0

    start, end = 1, x
    while start + 1 < end:
        mid = start + (end - start) / 2
        if mid**2 == x:
            return mid
        elif mid**2 > x:
            end = mid
        else:
            start = mid

    return start

#源码分析
#    异常检测，先处理小于等于0的值。
#    使用二分搜索的经典模板，注意不能使用start < end, 否则在给定值1时产生死循环。
#    最后返回平方根的整数部分start.

#二分搜索过程很好理解，关键是最后的返回结果还需不需要判断？比如是取 start, end, 还是 mid? 我们首先来分析下二分搜索的循环条件，由while循环条件start + 1 < end可知，start和end只可能有两种关系，一个是end == 1 || end ==2这一特殊情况，返回值均为1，另一个就是循环终止时start恰好在end前一个元素。设值 x 的整数部分为 k, 那么在执行二分搜索的过程中 start≤k≤end start \leq k \leq endstart≤k≤end 关系一直存在，也就是说在没有找到 mid2==xmid^2 == xmid​2​​==x 时，循环退出时有 start<k<endstart < k < endstart<k<end, 取整的话显然就是start了。

#复杂度分析
#经典的二分搜索，时间复杂度为 O(logn)O(\log n)O(logn), 使用了start, end, mid变量，空间复杂度为 O(1)O(1)O(1).
#除了使用二分法求平方根近似解之外，还可使用牛顿迭代法进一步提高运算效率，欲知后事如何，请猛戳 求平方根sqrt()函数的底层算法效率问题 -- 简明现代魔法，不得不感叹算法的魔力！

'''
Question

Wood Cut
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k, return the maximum length of the small pieces.
Example

For L=[232, 124, 456], k=7, return 114.
Note

You couldn't cut wood into float length.
'''

#题解 - 二分搜索
#这道题要直接想到二分搜素其实不容易，但是看到题中 Challenge 的提示后你大概就能想到往二分搜索上靠了。首先来分析下题意，题目意思是说给出 n 段木材L[i], 将这 n 段木材切分为至少 k 段，这 k 段等长，求能从 n 段原材料中获得的最长单段木材长度。以 k=7 为例，要将 L 中的原材料分为7段，能得到的最大单段长度为114, 232/114 = 2, 124/114 = 1, 456/114 = 4, 2 + 1 + 4 = 7.

#理清题意后我们就来想想如何用算法的形式表示出来，显然在计算如2, 1, 4等分片数时我们进行了取整运算，在计算机中则可以使用下式表示： ∑i=1nL[i]l≥k\sum _{i = 1} ^{n} \frac {L[i]}{l} \geq k∑​i=1​n​​​l​​L[i]​​≥k

#其中 lll 为单段最大长度，显然有 1≤l≤max(L[i])1 \leq l \leq max(L[i])1≤l≤max(L[i]). 单段长度最小为1，最大不可能超过给定原材料中的最大木材长度。
#   Warning 注意求和与取整的顺序，是先求 L[i]/l的单个值，而不是先对L[i]求和。
#分析到这里就和题 Sqrt x 差不多一样了，要求的是 lll 的最大可能取值，同时 lll 可以看做是从有序序列[1, max(L[i])]的一个元素，典型的二分搜素！
#P.S. 关于二分搜索总结在 Binary Search 一小节，直接套用『模板二——最优化』即可。
def woodCut(self, L, k):
    if sum(L) < k:
        return 0

    start, end = 1, max(L)
    while start + 1 < end:
        mid = (start + end) / 2
        pieces_sum = sum(len_i / mid for len_i in L)
        if pieces_sum < k:
            end = mid
        else:
            start = mid

    if sum(len_i / end for len_i in L) >= k:
        return end
    return start

#源码分析
#定义私有方法C为切分为 x 长度时能否大于等于 k 段。若满足条件则更新lb, 由于 lb 和 ub 的初始化技巧使得我们无需单独对最后的 lb 和 ub 单独求和判断。九章算法网站上的方法初始化为1和某最大值，还需要单独判断，虽然不会出bug, 但稍显复杂。这个时候lb, ub初始化为两端不满足条件的值的优雅之处就体现出来了。

#复杂度分析
#遍历求和时间复杂度为 O(n)O(n)O(n), 二分搜索时间复杂度为 O(logmax(L))O(\log max(L))O(logmax(L)). 故总的时间复杂度为 O(nlogmax(L))O(n \log max(L))O(nlogmax(L)). 空间复杂度 O(1)O(1)O(1).

