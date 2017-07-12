'''
在某个程序中一方面不适合使用selenium+phantomjs的方式（要实现的功能比较难不适合）
因为只能用原生的phantomjs，但是这个问题他本身在极端情况下也有可能停止（在超时设置之前因为某些错误）

那么最佳方案就是用python单独开一个线程（进程）调用原生phantomjs，然后对这个线程进程进行超时控制。
这里用ping这个命令先做测试，
'''

import subprocess
from threading import Timer
import time

kill = lambda process: process.kill()

cmd = ["ping", "http://www.google.com"]
ping = subprocess.Popen(
    cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_timer = Timer(5, kill, [ping])#这里设定时间，和命令
try:
    my_timer.start()#启用
    stdout, stderr = ping.communicate()#获得输出
    #print stderr
    print(time.ctime())
finally:
    print(time.ctime())
    my_timer.cancel()

'''
Wed Jul 12 14:10:20 2017
Wed Jul 12 14:10:20 2017
'''