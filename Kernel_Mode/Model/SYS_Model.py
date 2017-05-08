'''
sys模块用于提供对解释器相关的操作

模块方法	解释说明
sys.argv	传递到Python脚本的命令行参数列表，第一个元素是程序本身路径
sys.executable	返回Python解释器在当前系统中的绝对路径
sys.exit([arg])	程序中间的退出，arg=0为正常退出
sys.path	返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform	返回操作系统平台名称，Linux是linux2，Windows是win32
sys.stdout.write(str)	输出的时候把换行符\n去掉
val = sys.stdin.readline()[:-1]	拿到的值去掉\n换行符
sys.version	获取Python解释程序的版本信息
'''
'''
位置参数
[root@ansheng ~]# cat scripts.py
'''
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
'''
[root@ansheng ~]# python scripts.py canshu1 canshu2
scripts.py
canshu1
canshu2
'''
'''
sys.argv[0]代表脚本本身，如果用相对路径执行则会显示脚本的名称，如果是绝对路径则会显示脚本名称；
程序中途退出
python在默认执行脚本的时候会由头执行到尾，然后自动退出，但是如果需要中途退出程序, 你可以调用sys.exit函数，它带有一个可选的整数参数返回给调用它的程序. 这意味着你可以在主程序中捕获对sys.exit的调用。（注：0是正常退出，其他为不正常，可抛异常事件供捕获!）

原脚本和输出的结果：
[root@iZ28i253je0Z sys]# cat sys-03.py
'''
print("hello word!")
print("your is pythoner")

'''
[root@iZ28i253je0Z sys]# python sys-03.py
hello word!
your is pythoner
执行脚本之后会输出，下面这两段内容：

hello word!
your is pythoner
然后我们在print "hello word！"之后让程序退出不执行print "your is pythoner"

[root@iZ28i253je0Z sys]# cat sys-03.py
'''
print("hello word!")
sys.exit()
print("your is pythoner")

'''
[root@iZ28i253je0Z sys]# python sys-03.py
hello word!
PS：sys.exit从python程序中退出，将会产生一个systemExit异常，可以为此做些清除除理的工作。这个可选参数默认正常退出状态是0，以数值为参数的范围为：0-127。其他的数值为非正常退出，还有另一种类型，在这里展现的是strings对象类型。
获取模块路径
在使用Python中用import、_import_导入模块的时候，那Python是怎么判断有没有这个模块的呢?
其实就是根据sys.path的路径来搜索你导入模块的名称。
'''
for i in sys.path:
    print(i)
'''
C:\Python35\lib\site-packages\pip-8.1.1-py3.5.egg
C:\Python35\python35.zip
C:\Python35\DLLs
C:\Python35\lib
C:\Python35
C:\Python35\lib\site-packages
获取当前系统平台
Linux
'''
sys.platform
# 'linux2'
# Windows

