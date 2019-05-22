import paramiko
import datetime
import os
from core import  file_client,file_server


def file_view():
    print('欢迎来到上传文件视图')
    file_client()
    file_server()
