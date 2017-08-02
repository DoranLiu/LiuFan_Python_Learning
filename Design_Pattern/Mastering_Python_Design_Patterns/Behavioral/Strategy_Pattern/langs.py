import pprint
from collections import namedtuple
from operator import attrgetter
'''
pprint和attrgetter模块。p
print模块用于美化输出一个数据结构， attrgetter用于通过属性名访问class或namedtuple的属性。
也可以使用一个lambda函数来替代使用attrgetter。
'''
if __name__ == '__main__':
    ProgrammingLang = namedtuple('ProgrammingLang', 'name ranking')
    stats = (('Ruby', 14), ('Javascript', 8), ('Python', 7),
             ('Scala', 31), ('Swift', 18), ('Lisp', 23))
    lang_stats = [ProgrammingLang(n, r) for n, r in stats]
    pp = pprint.PrettyPrinter(indent=5)
    pp.pprint(sorted(lang_stats, key=attrgetter('name')))
    print()
    pp.pprint(sorted(lang_stats, key=attrgetter('ranking')))
