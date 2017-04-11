'''
8.计数排序:

思路：
我们希望能线性的时间复杂度排序，如果一个一个比较，显然是不实际的，书上也在决策树模型中论证了，比较排序的情况为nlogn 的复杂度。
既然不能一个一个比较，我们想到一个办法，就是如果在排序的时候就知道他的位置，那不就是扫描一遍，把他放入他应该的位置不就可以了。
要知道他的位置，我们只需要知道有多少不大于他不就可以了吗？

性能分析：
最好，最坏，平均的时间复杂度O(n+k), 线性时间完成排序，且稳定。

优点：不需要比较函数，利用地址偏移，对范围固定在[0,k]的整数排序的最佳选择。是排序字节串最快的排序算法。
缺点：由于用来计数的数组的长度取决于待排序数组中数据的范围（等于待排序数组的最大值与最小值的差加上1），这使得计数排序对于数据范围很大的数组，需要大量时间和内存。

原理：
计数排序假设n个输入元素中的每一个都介于0和k之间的整数，k为n个数中最大的元素。
当 k = O(n) 时，计数排序的运行时间为θ(n)。
计数排序的基本思想是：对n个输入元素中每一个元素x，统计出小于等于x的元素个数，根据x的个数可以确定x在输出数组中的最终位置。
此过程需要引入两个辅助存放空间，存放结果的B[1...n]，用于确定每个元素个数的数组C[0...k]。

算法的具体步骤如下：
（1）根据输入数组A中元素的值确定k的值，并初始化C[1....k]= 0；
（2）遍历输入数组A中的元素，确定每个元素的出现的次数，并将A中第i个元素出现的次数存放在C[A[i]]中，然后C[i]=C[i]+C[i-1]，在C中确定A中每个元素前面有多个元素；
（3）逆序遍历数组A中的元素，在C中查找A中出现的次数，并结果数组B中确定其位置，然后将其在C中对应的次数减少1。
'''

# 演示
# https://www.cs.usfca.edu/~galles/visualization/CountingSort.html

from collections import defaultdict
import random

def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)  # Output and "counts"
    for x in A:
        C[key(x)].append(x)  # "Count" key(x)
    for k in range(min(C), max(C) + 1):  # For every key in the range
        B.extend(C[k])  # Add values in sorted order
    return B

seq = [random.randrange(100) for i in range(10)]
seq = counting_sort(seq)