import os,sys
import menu as menu

# 需求：记录用户在服务器的所有操作！！
#
# 1、需要一台主机当作堡垒机
# 2、所有用户只能登录堡垒机
# 3、登录堡垒机后，可以对远程服务器进行操作
# 4、记录用户的所有操作
# 　　【登录堡垒机】--> 【选择服务器】 --> 【操作服务器，并记录操作】
#
# 实现：
# 1、创建堡垒机用户
# 　　adduser xxx
#
# 2、用户登录堡垒机后，自动执行脚本
# 　　配置 .brashrc
# 　　添加 /usr/bin/python /home/wupeiqi/share/workspace/07day07/section_two/menu.py

msg = """
\033[42;1mWelcome using old boy's auditing system!\033[0m
"""
print (msg)

host_dic = {
    'zhangke': '10.0.0.137',
    'xiaoqing': '10.0.0.135',
    'hanxin' : '10.0.1.139'
}

while True:
    for hostname, ip in host_dic.items():
        print (hostname,ip)
    try:
        host = input('Please choose one server to login:').strip()
        if host == 'quit':
            print ("Goodbye!")
            break
    except KeyboardInterrupt:continue
    except EOFError:continue
    if len(host) ==0:continue
    if not host_dic.has_key(host) :
        print ('No host matched, try again.')
        continue
    print ('\033[32;1mGoing to connect \033[0m', host_dic[host])
    os.system("python demo.py %s" % host_dic[host])

menu