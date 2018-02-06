# !/usr/bin/python
import socket
ips = ['127.0.0.1:55579', '127.0.0.1:55578']
for num in ips:
    ip_port = ips.split(':')
    s = socket.socket()
    s.connect((ip_port[0], int(ip_port[1])))
    s.send('here you ddos command')
    print(s.recv(1024))
