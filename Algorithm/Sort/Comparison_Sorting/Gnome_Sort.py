'''
侏儒排序法：
只有一个while和一个索引范围0到len(seq)-1的索引变量，复杂度在 O(n)~O(n^2)
'''
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i],seq[i-1] = seq[i-1],seq[i]
            i -= 1

