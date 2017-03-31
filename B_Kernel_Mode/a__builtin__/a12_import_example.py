# import 加载和重载模块
# __import__ 函数加载模块

#---------------------------------------------------------------
# 动态导入所有以-plugin.py结尾的文件
import glob, os
modules = []
for module_file in glob.glob("*-plugin.py"):
    try:
        module_name, ext =os.path.splitext(os.path.basename(module_file))
        module = __import__(module_name)
        modules.append(module)
    except ImportError:
        pass # ignore broken modules
        # say hello to all modules
for module in modules:
    module.hello()
# 注意这个 plug-in 模块文件名中有个 "-" (hyphens). 这意味着你不能使用普通的 import 命令, 因为 Python 的辨识符不允许有 "-" .

#---------------------------------------------------------------
# 使用 __import__ 函数获得特定函数
def get_function_by_name(module_name, function_name):
    module = __import__(module_name)
    return getattr(module, function_name)
print (repr(get_function_by_name("dumbdbm", "open")))
'''
<function open at 0x7f7f800ee488>
'''

#---------------------------------------------------------------
# 使用 __import__ 函数实现延迟导入string
class LazyImport:
    def __init__(self, module_name):
        self.module_name = module_name
        self.module = None
    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module, name)

string = LazyImport("string")
print (string.lowercase)
'''
abcdefghijklmnopqrstuvwxyz
'''

#---------------------------------------------------------------
# 重新加载已加载模块的基本支持.
# 注意,当你重加载模块时, 它会被重新编译, 新的模块会代替模块字典里的老模块.
# 但是, 已经用原模块里的类建立的实例仍然使用的是老模块(不会被更新).
# 同样地, 使用 from-import 直接创建的到模块内容的引用也是不会被更新的.
import sys
import reload
reload(sys)
reload(sys)
# 加载三次sys模块


