'''
Question

Problem Statement:
Given an array of integers, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

Example:
numbers=[2, 7, 11, 15], target=9
return [1,2]
'''

#题解1 - 哈希表
#找两数之和是否为target, 如果是找数组中一个值为target该多好啊！遍历一次就知道了，我只想说，too naive... 难道要将数组中所有元素的两两组合都求出来与target比较吗？时间复杂度显然为 O(n2)O(n^2)O(n​2​​), 显然不符题目要求。找一个数时直接遍历即可，那么可不可以将两个数之和转换为找一个数呢？我们先来看看两数之和为target所对应的判断条件—— xi+xj=targetx_i + x_j = targetx​i​​+x​j​​=target, 可进一步转化为 xi=target−xjx_i = target - x_jx​i​​=target−x​j​​, 其中 iii 和 jjj 为数组中的下标。一段神奇的数学推理就将找两数之和转化为了找一个数是否在数组中了！可见数学是多么的重要...

#基本思路有了，现在就来看看怎么实现，显然我们需要额外的空间(也就是哈希表)来保存已经处理过的 xjx_jx​j​​(注意这里并不能先初始化哈希表，否则无法排除两个相同的元素相加为 target 的情况), 如果不满足等式条件，那么我们就往后遍历，并把之前的元素加入到哈希表中，如果target减去当前索引后的值在哈希表中找到了，那么就将哈希表中相应的索引返回，大功告成！
def twoSum(numbers, target):
    hashdict = {}
    for i, item in enumerate(numbers):
        if (target - item) in hashdict:
            return (hashdict[target - item] + 1, i + 1)
        hashdict[item] = i

    return (-1, -1)
#复杂度分析
#哈希表用了和数组等长的空间，空间复杂度为 O(n)O(n)O(n), 遍历一次数组，时间复杂度为 O(n)O(n)O(n).

'''
Question

3 Sum
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example:
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:
(-1, 0, 1)
(-1, -1, 2)
'''

#题解1 - 排序 + 哈希表 + 2 Sum
def threeSum(numbers):
    triplets = []
    length = len(numbers)
    if length < 3:
        return triplets

    numbers.sort()
    for i in xrange(length):
        target = 0 - numbers[i]
        # 2 Sum
        hashmap = {}
        for j in xrange(i + 1, length):
            item_j = numbers[j]
            if (target - item_j) in hashmap:
                triplet = [numbers[i], target - item_j, item_j]
                if triplet not in triplets:
                    triplets.append(triplet)
            else:
                hashmap[item_j] = j

    return triplets

#源码分析
#    异常处理，对长度小于3的直接返回。
#    排序输入数组，有助于提高效率和返回有序列表。
#    循环遍历排序后数组，先取出一个元素，随后求得 2 Sum 中需要的目标数。
#    由于本题中最后返回结果不能重复，在加入到最终返回值之前查重。
#由于排序后的元素已经按照大小顺序排列，且在2 Sum 中先遍历的元素较小，所以无需对列表内元素再排序。

#复杂度分析
#排序时间复杂度 O(nlogn), 两重for循环，时间复杂度近似为 O(n2)O(n^2)O(n​2​​)，使用哈希表(字典)实现，空间复杂度为 O(n)O(n)O(n).

'''
Question

3 Sum Closest:
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
# 题解1 - 排序 + 2 Sum + 两根指针 + 优化过滤
#和 3 Sum 的思路接近，首先对原数组排序，随后将3 Sum 的题拆解为『1 Sum + 2 Sum』的题，对于 Closest 的题使用两根指针而不是哈希表的方法较为方便。对于有序数组来说，在查找 Cloest 的值时其实是有较大的优化空间的。
def threeSumClosest(self, numbers, target):
    result = 2**31 - 1
    length = len(numbers)
    if length < 3:
        return result

    numbers.sort()
    larger_count = 0
    for i, item_i in enumerate(numbers):
        start = i + 1
        end = length - 1
        # optimization 1 - filter the smallest sum greater then target
        if start < end:
            sum3_smallest = numbers[start] + numbers[start + 1] + item_i
            if sum3_smallest > target:
                larger_count += 1
                if larger_count > 1:
                    return result

        while (start < end):
            sum3 = numbers[start] + numbers[end] + item_i
            if abs(sum3 - target) < abs(result - target):
                result = sum3

            # optimization 2 - filter the sum3 closest to target
            sum_flag = 0
            if sum3 > target:
                end -= 1
                if sum_flag == -1:
                    break
                sum_flag = 1
            elif sum3 < target:
                start += 1
                if sum_flag == 1:
                    break
                sum_flag = -1
            else:
                return result

    return result

#源码分析
#   leetcode 上不让自己导入sys包，保险起见就初始化了result为还算较大的数，作为异常的返回值。
#    对数组进行排序。
#    依次遍历排序后的数组，取出一个元素item_i后即转化为『2 Sum Cloest』问题。『2 Sum Cloest』的起始元素索引为i + 1，之前的元素不能参与其中。
#    优化一——由于已经对原数组排序，故遍历原数组时比较最小的三个元素和target值，若第二次大于target果断就此罢休，后面的值肯定越来越大。
#    两根指针求『2 Sum Cloest』，比较sum3和result与target的差值的绝对值，更新result为较小的绝对值。
#    再度对『2 Sum Cloest』进行优化，仍然利用有序数组的特点，若处于『一大一小』的临界值时就可以马上退出了，后面的元素与target之差的绝对值只会越来越大。

#复杂度分析
#对原数组排序，平均时间复杂度为 O(nlogn), 两重for循环，由于有两处优化，故最坏的时间复杂度才是 O(n^2), 使用了result作为临时值保存最接近target的值，两#处优化各使用了一个辅助变量，空间复杂度 O(1).


'''
Question:

Merge Sorted Array
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]
After merge, A will be filled as [1, 2, 3, 4, 5]
'''
#题解
#因为本题有 in-place 的限制，故必须从数组末尾的两个元素开始比较；否则就会产生挪动，一旦挪动就会是 O(n2)O(n^2)O(n​2​​) 的。 自尾部向首部逐个比较两个数组内的元素，取较大的置于数组 A 中。由于 A 的容量较 B 大，故最后 m == 0 或者 n == 0 时仅需处理 B 中的元素，因为 A 中的元素已经在 A 中，无需处理。
def mergeSortedArray(self, A, m, B, n):
    if B is None:
        return A

    index = m + n - 1
    while m > 0 and n > 0:
        if A[m - 1] > B[n - 1]:
            A[index] = A[m - 1]
            m -= 1
        else:
            A[index] = B[n - 1]
            n -= 1
        index -= 1

    # B has elements left
    while n > 0:
        A[index] = B[n - 1]
        n -= 1
        index -= 1

#源码分析
#第一个 while 只能用条件与。
#复杂度分析
#最坏情况下需要遍历两个数组中所有元素，时间复杂度为 O(n)O(n)O(n). 空间复杂度 O(1)O(1)O(1).

'''
Question

Merge Sorted Array II
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]
B=[2,4,5,6]
return [1,2,2,3,4,4,5,6]
'''
#题解
#上题要求 in-place, 此题要求返回新数组。由于可以生成新数组，故使用常规思路按顺序遍历即可。
def mergeSortedArray(self, A, B):
    if A is None or len(A) == 0:
        return B
    if B is None or len(B) == 0:
        return A

    C = []
    aLen, bLen = len(A), len(B)
    i, j = 0, 0
    while i < aLen and j < bLen:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    # A has elements left
    while i < aLen:
        C.append(A[i])
        i += 1

    # B has elements left
    while j < bLen:
        C.append(B[j])
        j += 1

    return C
#源码分析
#分三步走，后面分别单独处理剩余的元素。

#复杂度分析
#遍历 A, B 数组各一次，时间复杂度 O(n), 空间复杂度O(1).

'''
Question

Median
Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.
If there are even numbers in the array, return the N/2-th number after sorted.
Example
Given [4, 5, 1, 2, 3], return 3
Given [7, 9, 4, 5], return 5
'''

#题解
#寻找未排序数组的中位数，简单粗暴的方法是先排序后输出中位数索引处的数，但是基于比较的排序算法的时间复杂度为 O(nlogn)O(n \log n)O(nlogn), 不符合题目要求。线性时间复杂度的排序算法常见有计数排序、桶排序和基数排序，这三种排序方法的空间复杂度均较高，且依赖于输入数据特征（数据分布在有限的区间内），用在这里并不是比较好的解法。

#由于这里仅需要找出中位数，即找出数组中前半个长度的较大的数，不需要进行完整的排序，说到这你是不是想到了快速排序了呢？快排的核心思想就是以基准为界将原数组划分为左小右大两个部分，用在这十分合适。快排的实现见 Quick Sort, 由于调用一次快排后基准元素的最终位置是知道的，故递归的终止条件即为当基准元素的位置(索引)满足中位数的条件时(左半部分长度为原数组长度一半)即返回最终结果。由于函数原型中左右最小索引并不总是原数组的最小最大，故需要引入相对位置(长度)也作为其中之一的参数。若左半部分长度偏大，则下一次递归排除右半部分，反之则排除左半部分。
def median(self, nums):
    if not nums:
        return -1
    return self.helper(nums, 0, len(nums) - 1, (1 + len(nums)) / 2)

def helper(self, nums, l, u, size):
    if l >= u:
        return nums[u]

    m = l
    for i in xrange(l + 1, u + 1):
        if nums[i] < nums[l]:
            m += 1
            nums[m], nums[i] = nums[i], nums[m]

    # swap between m and l after partition, important!
    nums[m], nums[l] = nums[l], nums[m]

    if m - l + 1 == size:
        return nums[m]
    elif m - l + 1 > size:
        return self.helper(nums, l, m - 1, size)
    else:
        return self.helper(nums, m + 1, u, size - (m - l + 1))

#源码分析
#以相对距离(长度)进行理解，递归终止步的条件一直保持不变(比较左半部分的长度)。
#以题目中给出的样例进行分析，size 传入的值可为(len(nums) + 1) / 2, 终止条件为m - l + 1 == size, 含义为基准元素到索引为l的元素之间(左半部分)的长度(含)与(len(nums) + 1) / 2相等。若m - l + 1 > size, 即左半部分长度偏大，此时递归终止条件并未变化，因为l的值在下一次递归调用时并未改变，所以仍保持为size; 若m - l + 1 < size, 左半部分长度偏小，下一次递归调用右半部分，由于此时左半部分的索引值已变化，故size应改为下一次在右半部分数组中的终止条件size - (m - l + 1), 含义为原长度size减去左半部分数组的长度m - l + 1.

#复杂度分析
#和快排类似，这里也有最好情况与最坏情况，平均情况下，索引m每次都处于中央位置，即每次递归后需要遍历的数组元素个数减半，故总的时间复杂度为 O(n(1+1/2+1/4+...))=O(2n)O(n (1 + 1/2 + 1/4 + ...)) = O(2n)O(n(1+1/2+1/4+...))=O(2n), 最坏情况下为平方。使用了临时变量，空间复杂度为 O(1)O(1)O(1), 满足题目要求。


