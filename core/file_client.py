import requests
import os
import hashlib
import struct
import time

from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

with open('../db/file/test','r',encoding='utf-8') as f:
    for line in f:
        # md5加密
        line_md5=hashlib.md5()
        line_md5.update(line.encode('utf-8'))
        line_md5_hex=line_md5.hexdigest()
        client.send(bytes(line_md5_hex,encoding='gbk'))
        time.sleep(1)
client.close()