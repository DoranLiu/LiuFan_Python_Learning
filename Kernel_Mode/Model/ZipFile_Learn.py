'''
ZIP文件格式是通用的归档和压缩标准。该模块提供了创建，读取，写入，附加和列出ZIP文件的工具。

此模块目前不处理多磁盘ZIP文件。它可以处理使用ZIP64扩展名的ZIP文件（即ZIP大小超过4 GiB的ZIP文件）。它支持在ZIP存档中解密加密文件，但它目前无法创建加密文件。解密是非常慢的，因为它在本机Python而不是C中实现。

官方文档：https：//docs.python.org/3.5/library/zipfile.html

打包

>>> import zipfile
>>> import os
>>> os.system("ls -l")
总用量 0
0
# 以w的方式的时候是打开文件并清空，如果是a方式那么就是追加文件了
>>> z = zipfile.ZipFile('zip_file.zip', 'w')
# 把文件放入压缩包
>>> z.write('/tmp/folder/file.txt')
# 也可以是一个目录
>>> z.write('/tmp/folder/dir')
# 关闭文件
>>> z.close()
# 查看已经打包的文件
>>> os.system("ls -l zip_file.zip")
-rw-rw-r-- 1 ansheng ansheng 238 5月  26 17:08 zip_file.zip
0
追加一个文件

# 追加其实就是把模式w换成a
>>> z = zipfile.ZipFile('zip_file.zip', 'a')
>>> z.write('/tmp/folder/file.txt')
# 关闭文件
>>> z.close()
# 查看包内的文件
>>> z.namelist()
['tmp/folder/sc.pyc', 'tmp/folder/dir/', 'tmp/folder/file.txt']
查看压缩包内的所有文件

# z.namelist()获取压缩包内的所有文件，以列表形式返回
>>> z.namelist()
['tmp/folder/sc.pyc', 'tmp/folder/dir/', 'tmp/folder/file.txt']
解压

>>> z = zipfile.ZipFile('zip_file.zip', 'r')
# extractall把所有的文件解压到当前目录
>>> z.extractall()
>>> os.system("tree tmp/")
tmp/
└── folder
    ├── dir
    └── sc.pyc
2 directories, 1 file
0
解压一个单独的文件

>>> z = zipfile.ZipFile('zip_file.zip', 'r')
# 返回文件所在路径
>>> z.extract("tmp/folder/sc.pyc")
'/home/ansheng/tmp/folder/sc.pyc'
>>> os.system("tree tmp/")
tmp/
└── folder
    └── sc.pyc
1 directory, 1 file
0
'''