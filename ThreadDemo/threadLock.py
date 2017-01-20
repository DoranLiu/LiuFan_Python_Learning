import threading
import time

num = 0

def run(n):
    mlock = threading.Lock()
    mlock.acquire()
    time.sleep(1)
    global num
    num += 1
    print('%s\n' % num)
    mlock.release()

mlock = threading.BoundedSemaphore(4) #最多允许几个进程同时运行

for i in range(10):
    t = threading.Thread(target=run,args=(i,))
    t.start()