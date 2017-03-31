'''
pkgutil
如果要获取包里面的所有模块列表，不应该用os.listdir()，而是pkgutil模块。
'''

'''
假设文件结构如下：
test <dir>
  |_ __init__.py
  |_ add.py
  |_ user.py
  |
  |_ a <dir>
  .  |_ __init__.py
  .  |_ sub.py
  |
  |_ b <dir>
     |_ __init__.py
     |_ sub.py
'''

import pkgutil, test
for _, name, ispkg in pkgutil.walk_packages(test.__path__, test.__name__ + "."):
    print ("name: {0:12}, is_sub_package: {1}".format(name, ispkg))

# name: test.a    , is_sub_package: True
# name: test.add    , is_sub_package: False
# name: test.b  , is_sub_package: True
# name: test.user   , is_sub_package: False

for _, name, ispkg in pkgutil.iter_modules(test.__path__, test.__name__ + "."):
     print ("name: {0:12}, is_sub_package: {1}".format(name, ispkg))

# name: test.a      , is_sub_package: True
# name: test.a.sub  , is_sub_package: False
# name: test.add    , is_sub_package: False
# name: test.b      , is_sub_package: True
# name: test.b.sub  , is_sub_package: False
# name: test.user   , is_sub_package: False