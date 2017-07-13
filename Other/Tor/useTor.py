import socket
import socks
import requests

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9052)
socket.socket = socks.socksocket

print(requests.get('http://ifconfig.me/ip').text)
