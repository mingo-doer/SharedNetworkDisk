import requests
import os
import hashlib
import struct

from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(5)

conn, client_address = server.accept()
while True:
    res = conn.recv(512)
    if res:
        res1=struct.pack('25s',res)
        print(res1)
conn.close()
server.close()


