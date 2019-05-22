from core import admin,file

fun_dict={
    '1':admin.admin_view,
    '2':file.file_view
}

def run():
    while True:
        # 其实这里应该是用户先注册登录后才能上传。考虑到可以在前端进行处理判断，这里就先实现主要功能
        print('''
        选择你要进入的功能模块：
        1：登录注册
        2：上传文件
        ''')
        choice=input('请输入角色').strip()
        if choice not in fun_dict :continue
        fun_dict[choice]()