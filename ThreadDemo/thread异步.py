import threading
import time

def producer():
    print(u'等人来买包子 1')
    event.wait()
    event.clear()
    print(u'有人为了包子来了 3')
    print(u'等我做。4')
    time.sleep(5)
    print('包子好了 6')
    event.set()

def customer():
    print(u'我去买包子 2')
    event.set()
    time.sleep(2)

    print('等包子做好 5')
    while True:
        if event.isSet():
            print(u'真好吃 7')
        else:
            print('怎么还没好')
            time.sleep(1)

    print(event.wait())

event = threading.Event()
p = threading.Thread(target=producer)
c = threading.Thread(target=customer)
p.start()
c.start()