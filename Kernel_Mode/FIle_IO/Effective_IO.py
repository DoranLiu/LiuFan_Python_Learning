'''
如何设置文件的缓冲?
如何将文件映射到内存?
如何访问文件的状态？
如何使用临时文件？
'''

'''
如何设置文件的缓冲?

将文件内容写入到硬盘设备时，使用系统调用，这类I/O操作的时间很长，为了减少I/O操作的次数，
文件通常使用缓冲区（有足够多的数据才进行系统调用），文件的缓存行为，分为全缓冲、行缓存、无缓冲。
'''

# 全缓冲：
# open函数的buffering设置为大于1的整数n，n为缓冲区大小
f = open('demo2.txt', 'w', buffering=2048)
f.write('+' * 1024)
f.write('+' * 1023)
# 大于2048的时候就写入文件
f.write('-' * 2)
f.close()

# 行缓冲：open函数的buffering设置为1
f = open('demo3.txt', 'w', buffering=1)
f.write('abcd')
f.write('1234')
# 只要加上\n就写入文件中
f.write('\n')
f.close()

# 无缓冲：open函数的buffering设置为0
f = open('demo4.txt', 'w', buffering=0)
f.write('a')
f.write('b')
f.close()

'''
如何将文件映射到内存?

在访问某些二进制文件时，希望能把文件映射到内存中，可以实现随机访问.(framebuffer设备文件)
某些嵌入式设备，寄存器呗编址到内存地址空间，我们可以映射/dev/mem某范围，去访问这些寄存器
如果多个进程映射到同一个文件，还能实现进程通信的目的

解决方案
使用标准库中的mmap模块的mmap()函数，它需要一个打开的文件描述符作为参数
'''
import mmap
import os
f = open('demo.bin','r+b')
# 获取文件描述符
f.fileno()
m = mmap.mmap(f.fileno(),0,access=mmap.ACCESS_WRITE)
type(m)
# <type 'mmap.mmap'>
# 可以通过索引获取内容
m[0]

'''
如何访问文件的状态？

在某些项目中，我们需要获得文件状态，例如：

文件的类型(普通文件、目录、符号链接、设备文件…)
文件的访问权限
文件的最后的访问/修改/节点状态更改时间
普通文件的大小
'''

import os
s = os.stat('files')
print(s)
# posix.stat_result(st_mode=33188, st_ino=267646, st_dev=51713L, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1473996947, st_mtime=1473996947, st_ctime=1473996947)
print(s.st_mode)
# 33188
import stat
# stat有很多S_IS..方法来判断文件的类型
stat.S_ISDIR(s.st_mode)
'False'
# 普通文件
stat.S_ISREG(s.st_mode)
'True'
# 访问时间
s.st_atime
# 修改时间
s.st_mtime
# 状态更新时间
s.st_ctime
# 获取普通文件的大小
s.st_size

# 标准库中os.path下的一些函数，文件类型判断
os.path.isdir('dirs')
os.path.islink('lockfile')
os.path.isfile('files')

# 文件三个时间
os.path.getatime('files')
os.path.getmtime('files')
os.path.getctime('files')

# 获取文件大小
os.path.getsize('files')


'''
如何使用临时文件？

某项目中，我们从传感器采集数据，每收集到1G数据后，做数据分析，最终只保存分析结果，
这样很大的临时数据如果常驻内存，将消耗大量内存资源，我们可以使用临时文件存储这些临时数据(外部存储)
临时文件不用命名，且关闭后会自动被删除
'''

# 使用标准库中的tempfile下的TemporaryFile, NamedTemporaryFile
from tempfile import TemporaryFile, NamedTemporaryFile
# 访问的时候只能通过对象f来进行访问
f = TemporaryFile()
f.write('abcdef' * 100000)
# 访问临时数据
f.seek(0)
f.read(100)
'abcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd'
ntf = NamedTemporaryFile()
# 如果要让每次创建NamedTemporaryFile()对象时不删除文件，可以设置NamedTemporaryFile(delete=False)
print(ntf.name)
# 返回当前临时文件在文件系统中的路径
'/tmp/tmppNvBu2'