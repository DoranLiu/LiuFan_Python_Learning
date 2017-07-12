import time
import signal

'''
自定义函数的死锁or超时处理
python是顺序执行的，但是如果下一句话可能导致死锁（比如一个while（1））那么如何强制让他超时呢？
他本身如果没有带有超时设置的话，就要自己运行信号（import signal）来处理.
'''

def test(i):
    time.sleep(0.999)#模拟超时的情况
    print("%d within time"%(i))
    return i

def fuc_time(time_out):
    # 此为函数超时控制，替换下面的test函数为可能出现未知错误死锁的函数
    def handler(signum, frame):
        raise AssertionError
    try:
        signal.signal(signal.SIGALRM, handler)
        signal.alarm(time_out)#time_out为超时时间
        temp = test(1) #函数设置部分，如果未超时则正常返回数据
        return temp
    except AssertionError:
        print("%d timeout"%(i))# 超时则报错

if __name__ == '__main__':
    for i in range(1,10):
        fuc_time(1)

'''
1 timeout
2 timeout
1 within time
4 timeout
1 within time
6 timeout
7 timeout
8 timeout
1 within time
'''