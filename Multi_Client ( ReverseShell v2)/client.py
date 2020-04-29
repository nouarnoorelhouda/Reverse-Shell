import socket
import os
import subprocess

s = socket.socket()
host = '104.236.209.167'
port = 9999

s.connect((host, port))

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
