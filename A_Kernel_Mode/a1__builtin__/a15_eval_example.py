# Python 提供了在程序中与解释器交互的多种方法.
# 例如 eval 函数将一个字符串作为 Python 表达式求值. 你可以传递一串文本, 简单的表达式, 或者使用内建 Python 函数.

# 1. eval
# 2. eval安全


#---------------------------------------------------------------
# 使用 eval 函数--回归本来样貌
def dump(expression):
    result = eval(expression)
    print (expression, "=>", result, type(result))
dump("1")
dump("1.0")
dump("'string'")
dump("1.0 + 2.0")
dump("'*' * 10")
dump("len('world')")
'''
1 => 1 <type 'int'>
1.0 => 1.0 <type 'float'>
'string' => string <type 'str'>
1.0 + 2.0 => 3.0 <type 'float'>
'*' * 10 => ********** <type 'str'>
len('world') => 5 <type 'int'>
'''

#---------------------------------------------------------------
# 要注意字符串来源的安全性
# 为保证字符串的安全性，可以给eval函数传递第2个参数, 一个定义了该表达式求值时名称空间的字典.

# 安全地使用 eval 函数求值
print (eval("_ _import_ _('os').getcwd()", {}))
print (eval("_ _import_ _('os').remove('file')", {"_ _builtins_ _": {}}))
'''
Python 在求值前会检查这个字典, 如果没有发现名称为 __builtins__ 的变量(复数形式), 它就会添加一个
即使这样, 你仍然无法避免针对 CPU 和内存资源的攻击.
比如:eval("'*'*1000000*2*2*2*2*2*2*2*2*2") 在执行后会使你的程序耗尽系统资源.
'''
