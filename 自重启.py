'''
比如程序在某种情况下报错多次，那么满足条件后，让其重启即可解决大多数问题，当然这只不过是治标不治本而已
如果这个程序重启没有大问题（例如读队列类型）那么自重启这是最省力的方式之一。
'''

import time,sys,os
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

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