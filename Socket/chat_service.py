'''
多并发
'''

import socket
# 创建一个socket对象
sk = socket.socket()
# 绑定允许连接的IP地址和端口
sk.bind(('127.0.0.1', 6053,))
# 服务端允许起来之后，限制客户端连接的数量，如果超过五个连接，第六个连接来的时候直接断开第六个。
sk.listen(5)

while True:
    # 会一直阻塞，等待接收客户端的请求，如果有客户端连接会获取两个值，conn=创建的连接，address=客户端的IP和端口
    conn, address = sk.accept()
    # 当用户连接过来的时候就给用户发送一条信息，在Python3里面需要把发送的内容转换为字节
    conn.sendall(bytes("你好，欢迎登陆！", encoding="utf-8"))
    while True:
        # 输出等待客户端发送内容
        print("正在等待Client输入内容......")
        # 接收客户端发送过来的内容
        ret_bytes = conn.recv(1024)
        # 转换成字符串类型
        ret_str = str(ret_bytes, encoding="utf-8")
        # 输出用户发送过来的内容
        print(ret_str)
        # 如果用户输入的是q
        if ret_str == "q":
            # 则退出循环，等待下个用户输入
            break
        # 给客户端发送内容
        inp = input("Service请输入要发送的内容>>> ")
        conn.sendall(bytes(inp, encoding="utf-8"))


'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=多并发版本=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''
利用socketserver实现多并发，socketserver内部会调用socket模块进行功能上的实现
'''
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        conn.sendall(bytes("你好，欢迎登陆！", encoding="utf-8"))
        while True:
            # 输出等待客户端发送内容
            print("正在等待Client输入内容......")
            # 接收客户端发送过来的内容
            ret_bytes = conn.recv(1024)
            # 转换成字符串类型
            ret_str = str(ret_bytes, encoding="utf-8")
            # 输出用户发送过来的内容
            print(ret_str)
            # 如果用户输入的是q
            if ret_str == "q":
                # 则退出循环，等待下个用户输入
                break
            # 给客户端发送内容
            inp = input("Service请输入要发送的内容>>> ")
            conn.sendall(bytes(inp, encoding="utf-8"))

if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(('127.0.0.1', 999, ), MyServer)
    server.serve_forever()
