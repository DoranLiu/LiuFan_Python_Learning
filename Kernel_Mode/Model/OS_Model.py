'''
OS模块：

该模块提供了使用操作系统相关功能的便携式方法。如果您只想读或写一个文件，请参阅open（），如果要操作路径，请参阅os.path模块，如果要读取命令行中所有文件中的所有行，请参阅fileinput模块。要创建临时文件和目录，请参阅tempfile模块，对于高级文件和目录处理，请参阅shutil模块
OS模块常用方法

模块方法	说明
os.getcwd（）	获取当前工作目录，即当前的Python脚本工作的目录路径
os.chdir（“目录名称”）	改变当前脚本工作目录;相当于壳下CD
os.curdir	返回当前目录：（'。'）
os.pardir	获取当前目录的父目录字符串名:( '..'）
os.makedirs（ 'dirname1 / dirname2'）	可生成多层递归目录
os.removedirs（ 'dirname1'）	若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir（ '目录名称'）	生成单级目录;相当于shell中mkdir dirname
os.rmdir（ '目录名称'）	删除单级空目录，若目录不为空则无法删除，报错;相当于shell中rmdir dirname
os.listdir（ '目录名称'）	列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove（）	删除一个文件
os.rename（“使用oldName”，” NEWNAME”）	重命名文件/目录
os.stat（ '路径/文件名'）	获取文件/目录信息
os.sep	输出操作系统特定的路径分隔符，赢下为\\，LINUX下为/
os.linesep	输出当前平台使用的行终止符，赢下为\t\n，LINUX下为\n
os.pathsep	输出用于分割文件路径的字符串
os.name	输出字符串指示当前使用平台.win-> nt; Linux的>posix
os.system（“bash命令”）	运行外壳命令，直接显示
os.environ	获取系统环境变量
os.path.abspath则（路径）	返回路径规范化的绝对​​路径
os.path.split这样的（路径）	将通道分割成目录和文件名二元组返回
os.path.dirname（路径）	返回路径的目录。其实就是os.path.split这样（路径）的第一个元素
os.path.basename（路径）	返回路径最后的文件名。如何路径以／或\结尾，那么就会返回空值。即os.path.split这样（路径）的第二个元素
os.path.exists（路径）	如果路径存在，返回真;如果路径不存在，返回假
os.path.isabs（路径）	如果路径是绝对路径，返回真
os.path.isfile（路径）	如果路径是一个存在的文件，返回真否则，返回假
os.path.isdir（路径）	如果路径是一个存在的目录，则返回真。否则返回假
os.path.join（path1 [，path2 [，...]]）	将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime（路径）	返回路径所指向的文件或者目录的最后存取时间
os.path.getmtime（路径）	返回路径所指向的文件或者目录的最后修改时间
'''
'''
# 常用方法实例
'''
import os
# 获取当前工作目录
# 获取的进入python时的目录
os.getcwd()
'/root'
# 工作改变目录到/tmp下
 # 当前目录是/root
os.getcwd()
'/root'
 # 切换到/tmp下
os.chdir("/tmp")
 # 当前目录变成了/tmp
os.getcwd()
'/tmp'

# 电子杂志/root目录下的所有文件，包括隐藏文件
os.listdir('/root')
['.cshrc', '.bash_history', '.bash_logout', '.viminfo', '.bash_profile', '.tcshrc', 'scripts.py', '.bashrc', 'modules']

# 删除/tmp目录下的os.txt文件
os.chdir("/tmp")
os.getcwd()
'/tmp'
os.listdir('./')
['.ICE-unix', 'yum.log']
os.remove("yum.log")
os.listdir('./')
['.ICE-unix']

# 查看/root目录信息
os.stat('/root')
'posix.stat_result(st_mode=16744, st_ino=130817, st_dev=2051L, st_nlink=3, st_uid=0, st_gid=0, st_size=4096, st_atime=1463668203, st_mtime=1463668161, st_ctime=1463668161)'

# 查看当前操作系统的平台
os.name
'posix'
# win - > nt，Linux - >posix

# 一段执行shell命令
# 执行的命令要写绝对路径
os.system("/usr/bin/whoami")
# root
# 0代表命令执行成功，如果命令没有执行成功则返回的是非0
0
# 组合一个路径
a1 = "/"
a2 = "root"
os.path.join(a1, a2)
'/root'