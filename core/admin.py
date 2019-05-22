from interface import admin_interface

admin_info = {
    'name': None
}

def admin_register():
    print('管理员注册')
    while True:
        username=input('请输入用户名(q退出)').strip()
        if username=='q':
            break
        pwd=input('请输入密码(q退出)').strip()
        if pwd=='q':
            break
        pwd1=input('请再次输入密码')
        if pwd==pwd1:
            flg,msg=admin_interface.admin_register_interface(username,pwd)
            if flg:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一样')

def admin_login():
    print('管理员登录')
    while True:
        username = input('请输入用户名').strip()
        password = input('请输入密码').strip()
        flag, msg = admin_interface.admin_login_interface(username, password)
        if flag:
            print(msg)
            admin_info['name'] = username
            break
        else:
            print(msg)

fun_dict={
    '1':admin_register,
    '2':admin_login,

}
def admin_view():
    print('欢迎来到管理员视图')
    while True:
        print('''
            1 管理员注册
            2 管理员登录
            
            ''')
        choice = input('输入功能模块').strip()
        fun_dict[choice]()