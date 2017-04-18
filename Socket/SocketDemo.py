'''
Socket是网络连接端点。例如当你的Web浏览器请求ansheng.me的网站时，你的Web浏览器创建一个socket并命令它去连接ansheng.me的Web服务器主机，Web服务器也对过来的请求在一个socket上进行监听。两端使用各自的socket来发送和接收信息。

在使用的时候，每个socket都被绑定到一个特定的IP地址和端口。IP地址是一个由4个数组成的序列，这4个数均是范围0~255中的值；端口数值的取值范围是0~65535。端口数小于1024的都是为众所周知的网络服务所保留的；最大的保留数被存储在socket模块的IPPORT_RESERVED变量中。

不是所有的IP地址都对世界的其它地方可见。实际上，一些是专门为那些非公共的地址所保留的（比如形如192.168.y.z或10.x.y.z）。地址127.0.0.1是本机地址；它始终指向当前的计算机。程序可以使用这个地址来连接运行在同一计算机上的其它程序。

IP地址不好记，你可以花点钱为特定的IP地址注册一个主机名或域名。域名服务器（DNS）处理名字到IP地址的映射。每个计算机都可以有一个主机名，即使它没有在官方注册。

Python 提供了两个基本的 socket 模块。

第一个是 Socket，它提供了标准的 BSD Sockets API。
第二个是 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

Socket对象

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

参数一：地址簇

参数	描述
socket.AF_INET	IPv4（默认）
socket.AF_INET6	IPv6
ocket.AF_UNIX	只能够用于单一的Unix系统进程间通信
参数二：类型

参数	描述
socket.SOCK_STREAM	流式socket , for TCP （默认）
socket.SOCK_DGRAM	数据报式socket , for UDP
socket.SOCK_RAW	原始套接字，普通的套接字无法处理ICMP、IGMP等网络报文，而SOCK_RAW可以；其次，SOCK_RAW也可以处理特殊的IPv4报文；此外，利用原始套接字，可以通过IP_HDRINCL套接字选项由用户构造IP头。
socket.SOCK_RDM	是一种可靠的UDP形式，即保证交付数据报但不保证顺序。SOCK_RAM用来提供对原始协议的低级访问，在需要执行某些特殊操作时使用，如发送ICMP报文。SOCK_RAM通常仅限于高级用户或管理员运行的程序使用。
socket.SOCK_SEQPACKET	可靠的连续数据包服务
参数三：协议

参数	描述
0	（默认）与特定的地址家族相关的协议,如果是 0 ，则系统就会根据地址格式和套接类别,自动选择一个合适的协议
Socket类方法

方法	描述
s.bind(address)	将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。
sk.listen(backlog)	开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。
sk.setblocking(bool)	是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。
sk.accept()	接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。
sk.connect(address)	连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。
sk.connect_ex(address)	同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061
sk.close()	关闭套接字连接
sk.recv(bufsize[,flag])	接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。
sk.recvfrom(bufsize[.flag])	与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
sk.send(string[,flag])	将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。
sk.sendall(string[,flag])	将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。内部通过递归调用send，将所有内容发送出去。
sk.sendto(string[,flag],address)	将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。
sk.settimeout(timeout)	设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。
sk.getpeername()	返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
sk.getsockname()	返回套接字自己的地址。通常是一个元组(ipaddr,port)
sk.fileno()	套接字的文件描述符


socket编程思路:

TCP服务端

创建套接字，绑定套接字到本地IP与端口
开始监听连接
进入循环，不断接受客户端的连接请求
然后接收传来的数据，并发送给对方数据
传输完毕后，关闭套接字
TCP客户端

创建套接字，连接远端地址
连接后发送数据和接收数据
传输完毕后，关闭套接字
'''
import socket

# 客户端

# 创建一个socket对象
sk = socket.socket()
# 绑定允许连接的IP地址和端口
sk.bind(('127.0.0.1', 6254, ))
# 服务端允许起来之后，限制客户端连接的数量，如果超过五个连接，第六个连接来的时候直接断开第六个。
sk.listen(5)
print("正在等待客户端连接....")
# 会一直阻塞，等待接收客户端的请求，如果有客户端连接会获取两个值，conn=创建的连接，address=客户端的IP和端口
conn, address = sk.accept()
# 输入客户端的连接和客户端的地址信息
print(address, conn)


# 服务端

# 创建一个socket对象
obj = socket.socket()
# 制定服务端的IP地址和端口
obj.connect(('127.0.0.1', 6254, ))
# 连接完成之后关闭链接
obj.close()