import paramiko
import datetime
import os
hostname='106.13.81.79'
username='admin'
port=22



def file_common():
    pass

def file_image():
    pass

def file_video():
    pass


fun_dict={
    '1':file_common,
    '2':file_image,
    '3':file_video

}
def file_view():
    print('欢迎来到上传文件视图')
    while True:
        print('''
                1 普通文件
                2 图片
                3 视频

                ''')
        choice = input('输入功能模块').strip()
        fun_dict[choice]()