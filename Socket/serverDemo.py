import socket

sk = socket.socket()
ip_port = ('127.0.0.1','9999')
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address = sk.accept()
    conn.send('hello')
    inp = input("请输入:")
    flag = True
    while flag:
        if  inp == "exit":
            flag = False

    conn.close()

###TCP
import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        conn.send('Hello')
        flag = True
        while flag:
            data = conn.recv(1024)
            print(data)
            if data == 'exit':
                flag = False
            conn.send('Bey')
        conn.close()

    def finish(self):
        pass

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
    server.server_forever()