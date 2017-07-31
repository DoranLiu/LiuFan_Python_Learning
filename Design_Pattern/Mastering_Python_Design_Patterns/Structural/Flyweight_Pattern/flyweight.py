# coding: utf-8
'''
享元模式
由于对象创建的开销，面向对象的系统可能会面临性能问题。
性能问题通常在资源受限的嵌 入式系统中出现，比如智能手机和平板电脑。
大型复杂系统中也可能会出现同样的问题，因为要 在其中创建大量对象(也可能是用户)，这些对象需要同时并存。

作为软件工程师，我们应该编写更好的软件来解决软件问题，而不是要求客户购买更多更好的硬件。
享元设计模式通过为相似对象引入数据共享来最小化内存使用，提升性能(请参考网页 [t.cn/RqrjNF3])。
一个享元(Flyweight)就是一个包含状态独立的不可变(又称固有的)数据的[GOF95，第219页]和网页[t.cn/RqrjOX3])。
'''
import random
from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


'''
由于之前已提到树的例子，那么就来看看如何实现它。
在这个例子中，我们将构造一小片水 果树的森林，小到能确保在单个终端页面中阅读整个输出。
然而，无论你构造的森林有多大，内存分配都保持相同。
下面这个Enum类型变量描述三种不同种类的水果树。
'''
class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


'''
main()函数展示了我们可以如何使用享元模式。
一棵树的年龄是1到30年之间的一个随机值。坐标使用1到100之间的随机值。
虽然渲染了18棵树，但仅分配了3棵树的内存。输出的最后一行证明当使用享元时，我们不能依赖对象的ID。
函数id()会返回对象的内存地址。
Python规范 并没有要求id()返回对象的内存地址，只是要求id()为每个对象返回一个唯一性ID，
不过 CPython(Python的官方实现)正好使用对象的内存地址作为对象唯一性ID。
在我们的例子中， 即使两个对象看起来不相同，但是如果它们属于同一个享元家族(在这里，家族由tree_type 14 定义)，那么它们实际上有相同的ID。
当然，不同ID的比较仍然可用于不同家族的对象，但这仅在客户端知道实现细节的情况下才可行(通常并非如此)。
'''
def main():
    rnd = random.Random()
    age_min, age_max = 1, 30    # 单位为年
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point))
        tree_counter += 1

    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))

    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))

if __name__ == '__main__':
    main()
