'''
8.计数排序:
计数排序假设n个输入元素中的每一个都介于0和k之间的整数，k为n个数中最大的元素。
当k=O(n)时，计数排序的运行时间为θ(n)。
计数排序的基本思想是：对n个输入元素中每一个元素x，统计出小于等于x的元素个数，根据x的个数可以确定x在输出数组中的最终位置。
此过程需要引入两个辅助存放空间，存放结果的B[1...n]，用于确定每个元素个数的数组C[0...k]。

算法的具体步骤如下：
（1）根据输入数组A中元素的值确定k的值，并初始化C[1....k]= 0；
（2）遍历输入数组A中的元素，确定每个元素的出现的次数，并将A中第i个元素出现的次数存放在C[A[i]]中，然后C[i]=C[i]+C[i-1]，在C中确定A中每个元素前面有多个元素；
（3）逆序遍历数组A中的元素，在C中查找A中出现的次数，并结果数组B中确定其位置，然后将其在C中对应的次数减少1。
'''

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