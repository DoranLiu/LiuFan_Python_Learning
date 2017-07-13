'''
比如程序在某种情况下报错多次，那么满足条件后，让其重启即可解决大多数问题，当然这只不过是治标不治本而已
如果这个程序重启没有大问题（例如读队列类型）那么自重启这是最省力的方式之一。
'''

import time,sys,os

def restart_program():
    # sys.executable 一个字符串给Python解释器的可执行二进制文件的绝对路径，在这样的系统上是有意义的。
    # 如果Python无法检索其可执行文件的真实路径，则为sys.executable空字符串None。
    python = sys.executable
    # execl(file,*args,)
    os.execl(python, python, * sys.argv)

    # sys.argv 传递给Python脚本的命令行参数列表。

if __name__ == "__main__":
    print('start...')
    print("3秒后,程序将结束...")
    time.sleep(3)
    restart_program()

'''
start...
3秒后,程序将结束...
start...
3秒后,程序将结束...
start...
3秒后,程序将结束...
'''