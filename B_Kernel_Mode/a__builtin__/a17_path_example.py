'''
__path__
某些时候，包内的文件太多，需要分类存放到多个目录中，但不想拆分成新的包或子包。
这么做是允许的，只要在__init__.py中用__path__指定所有目录的全路径即可(目录可放在包外)。
'''

'''
假如文件层次如下：
test <dir>
  |_ __init__.py
  |
  |_ a <dir>
  .  |_ add.py
  |
  |_ b <dir>
     |_ sub.py
'''
# 在__init__.py文件中写入
__path__ = ["/home/yuhen/py/test/a", "/home/yuhen/py/test/b"]

# 稍微改进下。
# 可以用os.listdir()扫描全部目录，自动形成路径列表。
from os.path import abspath, join
subdirs = lambda *dirs: [abspath(join(__path__[0], sub)) for sub in dirs]
__path__ = subdirs("a", "b")
