from threading import Thread
import time
def Foo(arg):
    for ite in range(10):
        print(ite)
        time.sleep(1)
    print(arg)

print('--------start------------')
t1 = Thread(target=Foo,args=('Hello1',))

# t1.setDaemon(True) #在start之前
t1.start()
t1.join(5) # 等待时间
print(t1.isDaemon())
print(t1.getName())
print('---------stop-------------')
