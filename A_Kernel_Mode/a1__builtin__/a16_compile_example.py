# -*- coding:utf-8 -*-

# 编译和执行代码

# eval函数只针对简单的表达式. 如果要处理大块的代码, 你应该使用 compile和 exec 函数

# 1. compile
# 2. exec

#---------------------------------------------------------------
# 使用 compile 函数检查语法
NAME = "script.py"
BODY =""" prnt 'owl-stretching time' """
try:
    compile(BODY,NAME, "exec")
except SyntaxError as s:
    print ("syntax error:", s, "in", NAME)
'''
syntax error: unexpected indent (script.py, line 1) in script.py
'''

#---------------------------------------------------------------
# 成功执行后, compile函数会返回一个代码对象, 你可以使用 exec 语句执行它.
BODY="""
print 'the ant, an introduction'
"""
code = compile(BODY,"<script>", "exec")
print (code)
exec (code)
'''
<code object <module> at 0x7f8bc1e35e30, file "<script>", line 2>
the ant, an introduction
'''

#---------------------------------------------------------------
# 下面的code可以在程序执行时实时地生成代码. write 方法用于添加代码,
# indent 和 dedent 方法用于控制缩进结构. 其他部分交给类来处理.
import sys, string
class CodeGeneratorBackend:
    "Simple code generator for Python"
    def begin(self, tab="/t"):
        self.code = []
        self.tab = tab
        self.level = 0

    def end(self):
        self.code.append("") # make sure there's a newline at the end
        return compile(string.join(self.code, "/n"), "<code>", "exec")

    def write(self, string):
        self.code.append(self.tab * self.level + string)

    def indent(self):
        self.level = self.level + 1
        # in 2.0 and later, this can be written as: self.level += 1

    def dedent(self):
        if self.level == 0:
            raise (SyntaxError, "internal error in code generator")
        self.level = self.level - 1
        # or: self.level -= 1

c = CodeGeneratorBackend()
c.begin()
c.write("for i in range(5):")
c.indent()
c.write("print 'code generation made easy!'")
c.dedent()
exec (c.end())







