'''
Question：
Given a string, determine if it is a palindrome.给定一个字符串，确定是否是回文。
considering only alphanumeric characters and ignoring cases.只考虑数字字母，忽略大小写。

Example:
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome
'''
#字符串的回文判断问题，由于字符串可随机访问，故逐个比较首尾字符是否相等最为便利，即常见的『两根指针』技法。
def isPalindrome(s):
     #空字符也是palindrome
    if not s:
        return True

    l, r = 0, len(s) - 1

    while l < r:
          # 从string左端开始，如果是空格就右移，找到最左边第一个合法字符(字母或者字符)
        if not s[l].isalnum(): # isalnum:如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
            l += 1
            continue
          # 从string右端开始，如果是空格就左移，找到最右边第一个合法字符(字母或者字符)
        if not s[r].isalnum():
            r -= 1
            continue
        # case insensitive compare，如果相同，就继续向中间移动
        if s[l].lower() == s[r].lower():
            l += 1
            r -= 1
        else:
            return False
    return True

# 两根指针遍历一次，时间复杂度 O(n) 空间复杂度 O(1)

'''
Question

Given a string S, find the longest palindromic(反复，回文) substring in S.
You may assume that the maximum length of S is 1000,and there exists one unique(唯一的) longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".
'''
# 穷竭搜索
#最简单的方案，穷举所有可能的子串，判断子串是否为回文，使用一变量记录最大回文长度，若新的回文超过之前的最大回文长度则更新标记变量并记录当前回文的起止索引，最后返回最长回文子串。
def longestPalindrome(s):
    # 如果s为空
    if not s:
        return ""

    n = len(s)
    longest, left, right = 0, 0, 0
    for i in xrange(0, n):
        for j in xrange(i + 1, n + 1):
            substr = s[i:j]
            if self.isPalindrome(substr) and len(substr) > longest: # 是回文，且比之前的长度大
                longest = len(substr) # 标记最长子串长度
                left, right = i, j
    # construct longest substr
    result = s[left:right] # 使用left, right作为子串的起止索引，用于最后构造返回结果，避免中间构造字符串以减少开销。
    return result

def isPalindrome(s):
    if not s:
        return False
    # reverse compare
    return s == s[::-1]

#穷举所有的子串，每次判断字符串是否为回文，复杂度为 O(n), 故总的时间复杂度为 O(n^3). 故大数据集下可能 TLE. 使用了substr作为临时子串，空间复杂度为 O(n).

# -*- coding:utf-8 -*-
import collections

'''
Question1：
在字符串内查找完全匹配的字符串的初始位置
'''
# 对于字符串查找问题，可使用双重for循环解决，效率更高的则为KMP算法。
# 双重 for 循环的使用需要考虑目标字符串比源字符串短的可能，所以对目标字符串的循环肯定是必要的，那么可以优化的地方就在于如何访问源字符串了。
def strStr(source, target):
    # 首先要两个字符串都不为空
    if source is None or target is None:
        return -1
    # 更为高效的方案则为仅遍历源字符串中有可能和目标字符串匹配的部分索引。
    for i in range(len(source) - len(target) + 1): # source剩下的target长度的字符就不必匹配了。
        for j in range(len(target)): # 遍历target的字符
            if source[i + j] != target[j]: # 一个一个的看是否完全相等
                break
        else:  # no break
            return i
    return -1
# 双重for 循环，时间复杂度最坏情况下为 O((n-m) * m)

'''
Question2_1：
Two Strings Are Anagrams
判断两个字符串是否互为变位词，若区分大小写，考虑空白字符时，直接来理解可以认为两个字符串的拥有各不同字符的数量相同。
'''
# 对于比较字符数量的问题常用的方法为遍历两个字符串，统计其中各字符出现的频次，若不等则返回false. 有很多简单字符串类面试题都是此题的变形题。
def anagram_1(s, t):
    return collections.Counter(s) == collections.Counter(t)
# 两个字符串长度不等时必不可能为变位词(需要注意题目条件灵活处理)。
# 初始化含有256个字符的计数器数组。对字符串 s 自增，字符串 t 递减，再次遍历判断letterCount数组的值，小于0时返回false.
# 在字符串长度较长(大于所有可能的字符数)时，还可对第二个for循环做进一步优化，即t.size() > 256时，使用256替代t.size(), 使用i替代t[i].

# 复杂度分析两次遍历字符串，时间复杂度最坏情况下为 O(n), 使用了额外的数组，空间复杂度 O(1).

'''
Question2_2：
另一直接的解法是对字符串先排序，若排序后的字符串内容相同，则其互为变位词。
'''
def anagram_2(s, t):
    return sorted(s) == sorted(t)
# 对字符串 s 和 t 分别排序，而后比较是否含相同内容。对字符串排序时可以采用先统计字频再组装成排序后的字符串，效率更高一点。

'''
Question3：
Compare Strings
问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，故返回false.
'''
def compare_strings(A, B):
    # return a dict with default value set to 0
    letters = collections.defaultdict(int)
    for a in A:
        letters[a] += 1

    for b in B:
        if b not in letters:
            return False
        elif letters[b] <= 0:
            return False
        else:
            letters[b] -= 1
    return True
'''
异常处理，B 的长度大于 A 时必定返回false, 包含了空串的特殊情况。
    使用额外的辅助空间，统计各字符的频次。
复杂度分析
    遍历一次 A 字符串，遍历一次 B 字符串，时间复杂度最坏 O(2n), 空间复杂度为 O(26).
'''

'''
Question4：
Anagrams
'''
'''Given an array of strings, return all groups of strings that are anagrams.'''
# 双重for循环(TLE) 方法一
def anagrams_1(self, strs):
    if len(strs) < 2:
        return strs
    result = []
    visited = [False] * len(strs)
    for index1, s1 in enumerate(strs):
        hasAnagrams = False
        for index2, s2 in enumerate(strs):
            if index2 > index1 and not visited[index2] and self.isAnagrams(s1, s2):
                result.append(s2)
                visited[index2] = True
                hasAnagrams = True
        if not visited[index1] and hasAnagrams:
            result.append(s1)
    return result

def isAnagrams(self, str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False
'''strs 长度小于等于1时直接返回。
使用与 strs 等长的布尔数组表示其中的字符串是否被添加到最终的返回结果中。
双重循环遍历字符串数组，注意去重即可。
私有方法isAnagrams用于判断两个字符串是否互为变位词。
复杂度分析
私有方法isAnagrams最坏的时间复杂度为 O(2L), 其中 LL 为字符串长度。
双重for循环时间复杂度近似为 1/2(O(n^2)), n 为给定字符串数组数目。
总的时间复杂度近似为 O(n^2 L).
使用了Vector String "visited"，空间复杂度可认为是 O(n).'''

# 方法二
# 排序 + hashmap
'''只不过此时的 hashmap 的 key 为字符串，value 为该字符串在 vector 中出现的次数。两次遍历字符串数组，第一次遍历求得排序后的字符串数量，第二次遍历将排序后相同的字符串取出放入最终结果中。'''
def anagrams_2(self, strs):
    strDict = {}
    result = []
    for string in strs:
        if "".join(sorted(string)) not in strDict.keys():
            strDict["".join(sorted(string))] = 1
        else:
            strDict["".join(sorted(string))] += 1
    for string in strs:
        if strDict["".join(sorted(string))] > 1:
            result.append(string)
    return result
'''源码分析

第一次遍历字符串数组获得排序后的字符串计数器信息，第二次遍历字符串数组将哈希表中计数器值大于1的字符串取出。

leetcode 中题目 signature 已经有所变化，这里使用一对多的 HashMap 较为合适，使用 ArrayList 作为 value. Java 中对 String 排序可先将其转换为 char[], 排序后再转换为新的 String.

复杂度分析

遍历一次字符串数组，复杂度为 O(n), 对单个字符串排序复杂度近似为 O(LlogL). 两次遍历字符串数组，故总的时间复杂度近似为 O(nLlogL). 使用了哈希表，空间复杂度为 O(K), 其中 K 为排序后不同的字符串个数。'''

'''Longest Common Substring'''
'''Given two strings, find the longest common substring.
Return the length of it.'''
'''求最长公共子串，注意「子串」和「子序列」的区别！简单考虑可以使用两根指针索引分别指向两个字符串的当前遍历位置，若遇到相等的字符时则同时向后移动一位。'''
def longestCommonSubstring(self, A, B):
    # write your code here
    ans = 0
    for i in xrange(len(A)):
        for j in xrange(len(B)):
            l = 0
            while i + l < len(A) and j + l < len(B) \
                    and A[i + l] == B[j + l]:
                l += 1
            if l > ans:
                ans = l
    return ans



'''Rotate String'''
'''Given a string and an offset, rotate string by offset. (rotate from left to right)
常见的翻转法应用题，仔细观察规律可知翻转的分割点在从数组末尾数起的offset位置。先翻转前半部分，随后翻转后半部分，最后整体翻转。
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"'''
# immutable string
def rotateString_1(self, A, offset):
    if A is None or len(A) == 0:
        return A

    offset %= len(A)
    before = A[:len(A) - offset]
    after = A[len(A) - offset:]
    # [::-1] means reverse in Python
    A = before[::-1] + after[::-1]
    A = A[::-1]

    return A

# mutable list
def rotateString_2(self, A, offset):
    if A is None or len(A) == 0:
        return

    offset %= len(A)
    self.reverse(A, 0, len(A) - offset - 1)
    self.reverse(A, len(A) - offset, len(A) - 1)
    self.reverse(A, 0, len(A) - 1)

def reverse(self, str_l, start, end):
    while start < end:
        str_l[start], str_l[end] = str_l[end], str_l[start]
        start += 1
        end -= 1

'''异常处理，A为空或者其长度为0
offset可能超出A的大小，应模len后再用
三步翻转法
Python 虽没有提供字符串的翻转，但用 slice 非常容易实现，非常 Pythonic!

通常来说，字符串在各种编程语言中的实现一般为 immutable 的，对字符串做改变时往往会生成新的字符串，所以如果要达到空间复杂度为 O(1) 的效果，需要用可变数据结构来实现。

复杂度分析

翻转一次时间复杂度近似为 O(n)O(n), 原地交换的空间复杂度为 O(1)O(1), 非原地交换的空间复杂度为 O(n)O(n). 总共翻转3次，所以总的时间复杂度为 O(n)O(n), 空间复杂度为 O(1)O(1) 或者 O(n)O(n).

'''

if __name__ == '__main__':
    # print strStr('asdfghjkl','hj')
    print anagram_1('sdf','dfs')
    print anagram_2('sdf','sdf')
