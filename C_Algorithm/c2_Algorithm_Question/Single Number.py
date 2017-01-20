#Single Number
#找单数」系列题，技巧性较强，需要灵活运用位运算的特性。


'''
Question

Single Number II:
Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.
Example
Given [1,1,2,3,3,3,2,2,4,1] return 4
'''
#逐位处理
#上题 Single Number 用到了二进制中异或的运算特性，这题给出的元素数目为3*n + 1，因此我们很自然地想到如果有种运算能满足「三三运算」为0该有多好！对于三个相同的数来说，其相加的和必然是3的倍数，仅仅使用这一个特性还不足以将单数找出来，我们再来挖掘隐含的信息。以3为例，若使用不进位加法，三个3相加的结果为：
#0011
#0011
#0011
#----
#0033
#注意到其中的奥义了么？三个相同的数相加，不仅其和能被3整除，其二进制位上的每一位也能被3整除！因此我们只需要一个和int类型相同大小的数组记录每一位累加的结果即可。时间复杂度约为 O((3n+1)⋅sizeof(int)⋅8)O((3n+1)\cdot sizeof(int) \cdot 8)O((3n+1)⋅sizeof(int)⋅8)
def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return 0

    result = 0
    for i in xrange(32):
        bit_i_sum = 0
        for num in nums:
            bit_i_sum += ((num >> i) & 1)
        result |= ((bit_i_sum % 3) << i)
    return self.twos_comp(result, 32)

def twos_comp(self, val, bits):
    """
    compute the 2's compliment of int value val
    e.g. -4 ==> 11100 == -(10000) + 01100
    """
    return -(val & (1 << (bits - 1))) | (val & ((1 << (bits - 1)) - 1))

#源码解析
#    异常处理
#    循环处理返回结果result的int类型的每一位，要么自增1，要么保持原值。注意i最大可取 8⋅sizeof(int)−18 \cdot sizeof(int) - 18⋅sizeof(int)−1, 字节数=>位数的转换
#    对第i位处理完的结果模3后更新result的第i位，由于result初始化为0，故使用或操作即可完成
#Python 中的整数表示理论上可以是无限的（求出处），所以移位计算得到最终结果时需要转化为2的补码。此方法参考自 Two's Complement in Python

'''
Question

Single Number III
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;
For n=5, return false;

'''
#题解
#咋看起来挺简单的一道题目，可之前若是没有接触过神奇的位运算技巧遇到这种题就有点不知从哪入手了，咳咳，我第一次接触到这个题就是在七牛的笔试题中看到的
#简单点来考虑可以连除2求余，看最后的余数是否为1，但是这种方法无法在 O(1)O(1)O(1) 的时间内解出，所以我们必须要想点别的办法了。2的整数幂若用二进制来表示，则其中必只有一个1，其余全是0，那么怎么才能用一个式子把这种特殊的关系表示出来了？传统的位运算如按位与、按位或和按位异或等均无法直接求解，我就不卖关子了，比较下x - 1和x的关系试试？以x=4为例。
#0100 ==> 4
#0011 ==> 3
#两个数进行按位与就为0了！如果不是2的整数幂则无上述关系，反证法可证之。
def checkPowerOf2(self, n):
    if n < 1:
        return False
    else:
        return (n & (n - 1)) == 0

#源码分析
#除了考虑正整数之外，其他边界条件如小于等于0的整数也应考虑在内。在比较0和(n & (n - 1))的值时，需要用括号括起来避免优先级结合的问题。
#复杂度分析
#O(1)O(1)O(1).

'''
Question

Convert Integer A to Integer B
Determine the number of bits required to convert integer A to integer B

Example
Given n = 31, m = 14,return 2
(31)10=(11111)2
(14)10=(01110)2
'''
#题解
#比较两个数不同的比特位个数，显然容易想到可以使用异或处理两个整数，相同的位上为0，不同的位上为1，故接下来只需将异或后1的个数求出即可。容易想到的方法是移位后和1按位与得到最低位的结果，使用计数器记录这一结果，直至最后操作数为0时返回最终值。这种方法需要遍历元素的每一位，有咩有更为高效的做法呢？还记得之前做过的 O1 Check Power of 2 吗？x & (x - 1)既然可以检查2的整数次幂，那么如何才能进一步得到所有1的个数呢？——将异或得到的数分拆为若干个2的整数次幂，计算得到有多少个2的整数次幂即可。

#以上的分析过程对于正数来说是毫无问题的，但问题就在于如果出现了负数如何破？不确定的时候就来个实例测测看，以-2为例，(-2) & (-2 - 1)的计算如下所示(简单起见这里以8位为准)：
 11111110 <==> -2   -2 <==> 11111110
#+                          &
# 11111111 <==> -1   -3 <==> 11111101
#=                          =
# 11111101                   11111100
#细心的你也许发现了对于负数来说，其表现也是我们需要的——x & (x - 1)的含义即为将二进制比特位的值为1的最低位置零。逐步迭代直至最终值为0时返回。
#C/C++ 和 Java 中左溢出时会直接将高位丢弃，正好方便了我们的计算，但是在 Python 中就没这么幸运了，因为溢出时会自动转换类型，Orz... 所以使用 Python 时需要对负数专门处理，转换为求其补数中0的个数。
def bitSwapRequired(self, a, b):
    count = 0
    a_xor_b = a ^ b
    neg_flag = False
    if a_xor_b < 0:
        a_xor_b = abs(a_xor_b) - 1
        neg_flag = True
    while a_xor_b > 0:
        count += 1
        a_xor_b &= (a_xor_b - 1)

    # bit_wise = 32
    if neg_flag:
        count = 32 - count
    return count

#源码分析
#Python 中 int 溢出时会自动变为 long 类型，故处理负数时需要求补数中0的个数，间接求得原异或得到的数中1的个数。
#考虑到负数的可能，C/C++, Java 中循环终止条件为a_xor_b != 0，而不是a_xor_b > 0.
#复杂度分析
#取决于异或后数中1的个数，O(max(ones in a ^ b)).

'''
Question
Factorial Trailing Zeroes
 
Write an algorithm which computes the number of trailing zeros in n factorial.
Example
11! = 39916800, so the out should be 2
'''

#题解1 - Iterative
#找阶乘数中末尾的连零数量，容易想到的是找相乘能为10的整数倍的数，如 2×52 \times 52×5, 1×101 \times 101×10 等，遥想当初做阿里笔试题时遇到过类似的题，当时想着算算5和10的个数就好了，可万万没想到啊，25可以变为两个5相乘！真是蠢死了... 根据数论里面的知识，任何正整数都可以表示为它的质因数的乘积[^wikipedia]。所以比较准确的思路应该是计算质因数5和2的个数，取小的即可。质因数2的个数显然要大于5的个数，故只需要计算给定阶乘数中质因数中5的个数即可。原题的问题即转化为求阶乘数中质因数5的个数，首先可以试着分析下100以内的数，再试试100以上的数，聪明的你一定想到了可以使用求余求模等方法 :)
def trailingZeroes(self, n):
    if n < 0:
        return -1

    count = 0
    while n > 0:
        n /= 5
        count += n

    return count

#源码分析
#    异常处理，小于0的数返回-1.
#    先计算5的正整数幂都有哪些，不断使用 n / 5 即可知质因数5的个数。
#    在循环时使用 n /= 5 而不是 i *= 5, 可有效防止溢出。
#    Warning lintcode 和 leetcode 上的方法名不一样，在两个 OJ 上分别提交的时候稍微注意下。

#复杂度分析
#关键在于n /= 5执行的次数，时间复杂度 log5n\log_5 nlog​5​​n，使用了count作为返回值，空间复杂度 O(1)O(1)O(1).

'''
题解2 - Recursive
可以使用迭代处理的程序往往用递归，而且往往更为优雅。递归的终止条件为n <= 0.
'''
def trailingZeroes(n):
    if n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        return n / 5 + self.trailingZeroes(n / 5)

#源码分析
#这里将负数输入视为异常，返回-1而不是0. 注意使用递归时务必注意收敛和终止条件的返回值。这里递归层数最多不超过 log5n\log_5 nlog​5​​n, 因此效率还是比较高的。
#复杂度分析
#递归层数最大为 log5n\log_5 nlog​5​​n, 返回值均在栈上，可以认为没有使用辅助的堆空间。

'''
Question

Unique Binary Search Trees
 
Given n, how many structurally unique BSTs (binary search trees)
that store values 1...n?

Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
'''
#题解1 - 两重循环
#挺有意思的一道题，与数据结构和动态规划都有点关系。这两天在骑车路上和睡前都一直在想，始终未能找到非常明朗的突破口，直到看到这么一句话——『以i为根节点的树，其左子树由[0, i-1]构成， 其右子树由[i+1, n]构成。』这不就是 BST 的定义嘛！灵活运用下就能找到递推关系了。
#容易想到这道题的动态规划状态为 count[n], count[n] 表示到正整数 i 为止的二叉搜索树个数。容易得到 count[1] = 1, 根节点为1，count[2] = 2, 根节点可为1或者2。那么 count[3] 的根节点自然可为1，2，3. 如果以1为根节点，那么根据 BST 的定义，2和3只可能位于根节点1的右边；如果以2为根节点，则1位于左子树，3位于右子树；如果以3为根节点，则1和2必位于3的左子树。
#抽象一下，如果以 i 作为根节点，由基本的排列组合知识可知，其唯一 BST 个数为左子树的 BST 个数乘上右子树的 BST 个数。故对于 i 来说，其左子树由[0, i - 1]构成，唯一的 BST 个数为 count[i - 1], 右子树由[i + 1, n] 构成，其唯一的 BST 个数没有左子树直观，但是也有迹可循。对于两组有序数列「1, 2, 3] 和 [4, 5, 6]来说，这两个有序数列分别组成的 BST 个数必然是一样的，因为 BST 的个数只与有序序列的大小有关，而与具体值没有关系。所以右子树的 BST 个数为 count[n - i]，于是乎就得到了如下递推关系： count[i]=∑j=0i−1(count[j]⋅count[i−j−1])count[i] = \sum _{j = 0} ^{i - 1} (count[j] \cdot count[i - j - 1])count[i]=∑​j=0​i−1​​(count[j]⋅count[i−j−1])
#网上有很多用 count[3] 的例子来得到递推关系，恕本人愚笨，在没有从 BST 的定义和有序序列个数与 BST 关系分析的基础上，我是不敢轻易说就能得到如上状态转移关系的。
def numTrees(self, n):
    if n < 0:
        return -1

    count = [0] * (n + 1)
    count[0] = 1
    for i in xrange(1, n + 1):
        for j in xrange(i):
            count[i] += count[j] * count[i - j - 1]

    return count[n]

#源码分析
#    对 n 小于0特殊处理。
#    初始化大小为 n + 1 的数组，初始值为0，但对 count[0] 赋值为1.
#    两重 for 循环递推求得 count[i] 的值。
#    返回 count[n] 的值。
#由于需要处理空节点的子树，故初始化 count[0] 为1便于乘法处理。其他值必须初始化为0，因为涉及到累加操作。
#复杂度分析
#一维数组大小为 n + 1, 空间复杂度为 O(n+1)O(n + 1)O(n+1). 两重 for 循环等差数列求和累计约 n2/2n^2 / 2n​2​​/2, 故时间复杂度为 O(n2)O(n^2)O(n​2​​). 此题为 Catalan number 的一种，除了平方时间复杂度的解法外还存在 O(n)O(n)O(n) 的解法，欲练此功，先戳 Wikipedia 的链接。



