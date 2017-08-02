# coding: utf-8
'''
策略模式(Strategy pattern)鼓励使用多种算法来解决一个问题，其杀手级特性是能够在运 行时透明地切换算法(客户端代码对变化无感知)。
因此，如果你有两种算法，并且知道其中一 种对少量输入效果更好，另一种对大量输入效果更好，则可以使用策略模式在运行时基于输入数据决定使用哪种算法。

大多数问题都可以使用多种方法来解决。以排序问题为例，对于以一定次序把元素放入一个列
表，排序算法有很多。通常来说，没有公认最适合所有场景的算法(请参考网页[t.cn/RqrBZJQ])。
一些不同的评判标准能帮助我们为不同的场景选择不同的排序算法，其中应该考虑的有以下几个。
 需要排序的元素数量:这被称为输入大小。当输入较少时，几乎所有排序算法的表现都 很好，但对于大量输入，只有部分算法具有不错的性能。
 算法的最佳/平均/最差时间复杂度:时间复杂度是算法运行完成所花费的(大致)时间长 短，不考虑系数和低阶项1。这是选择算法的最常见标准，但这个标准并不总是那么充分。
 算法的空间复杂度:空间复杂度是充分地运行一个算法所需要的(大致)物理内存量。 在我们处理大数据或在嵌入式系统(通常内存有限)中工作时，这个因素非常重要。
 算法的稳定性:在执行一个排序算法之后，如果能保持相等值元素原来的先后相对次序， 则认为它是稳定的。
 算法的代码实现复杂度:如果两个算法具有相同的时间/空间复杂度，并且都是稳定的， 那么知道哪个算法更易于编码实现和维护也是很重要的。
可能还有更多的评判标准值得考虑，但重要的是，我们真的只能使用单个排序算法来应对所 有情况吗?答案当然不是。一个更好的方案是把所有排序算法纳为己用，然后使用上面提到的标 准针对当前情况选择最好的算法。这就是策略模式的目的。
'''
import time
SLOW = 3  # 单位为秒
LIMIT = 5   # 字符数
WARNING = 'too bad, you picked the slow algorithm :('


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


def allUniqueSort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srtStr = sorted(s)
    for (c1, c2) in pairs(srtStr):
        if c1 == c2:
            return False
    return True


def allUniqueSet(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def allUnique(s, strategy):
    return strategy(s)


def main():
    while True:
        word = None
        while not word:
            word = input('Insert word (type quit to exit)> ')
            if word == 'quit':
                print('bye')
                return

            strategy_picked = None
            strategies = {'1': allUniqueSet, '2': allUniqueSort}
            while strategy_picked not in strategies.keys():
                strategy_picked = input('Choose strategy: [1] Use a set, [2] Sort and pair> ')

                try:
                    strategy = strategies[strategy_picked]
                    print('allUnique({}): {}'.format(word, allUnique(word, strategy)))
                except KeyError as err:
                    print('Incorrect option: {}'.format(strategy_picked))

if __name__ == '__main__':
    main()
