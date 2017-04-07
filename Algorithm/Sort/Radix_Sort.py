'''
基数排序：Radix Sort

适用情况：
计数排序和桶排序都只是在研究一个关键字的排序，现在我们来讨论有多个关键字的排序问题。

假设我们有一些二元组(a,b)，要对它们进行以a 为首要关键字，b的次要关键字的排序。
我们可以先把它们先按照首要关键字排序，分成首要关键字相同的若干堆。
然后，在按照次要关键值分别对每一堆进行单独排序。
最后再把这些堆串连到一起，使首要关键字较小的一堆排在上面。
按这种方式的基数排序称为 MSD(Most Significant Dight) 排序。

第二种方式是从最低有效关键字开始排序，称为 LSD(Least Significant Dight)排序。
首先对所有的数据按照次要关键字排序，
然后对所有的数据按照首要关键字排序。

要注意的是，使用的排序算法必须是稳定的，否则就会取消前一次排序的结果。
由于不需要分堆对每堆单独排序，LSD 方法往往比 MSD 简单而开销小。
https://segmentfault.com/image?src=http://img.blog.csdn.net/20150312165029654&objectId=1190000002595152&token=995123acf45c3cbc9f8dd6929e68bc5e

通常，基数排序要用到计数排序或者桶排序。
使用计数排序时，需要的是Order数组。
使用桶排序时，可以用链表的方法直接求出排序后的顺序。

性能分析：
时间复杂度O（n） (实际上是O(d(n+k)) d是位数)

扩展：
问题：对[0,n^2-1]的 n 个整数进行线性时间排序。
思路：把整数转换为n进制再排序，每个数有两位，每位的取值范围是[0..n-1]，再进行基数排序

http://blog.csdn.net/mishifangxiangdefeng/article/details/7685839
'''

# 演示
# http://www.cs.usfca.edu/~galles/visualization/BucketSort.html