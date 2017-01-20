import socket

def hadle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 ok\r\n\r\n")
    client.send("Hello,alex")

def main():
    sock =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('localhost',8080))
    sock.listen(5)

    while True:
        connection,adress = sock.accept()
        hadle_request(connection)
        connection.close()

if __name__ == '__main__':
    main()
