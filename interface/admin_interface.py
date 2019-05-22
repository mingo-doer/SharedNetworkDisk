from db import models,db_hander
from lib import  common

logger = common.get_logger('admin')

def admin_register_interface(username,pwd):
    admin_obj=models.Admin.get_obj_by_name(username)
    if admin_obj:
        return False,'管理员已存在'
    else:
        models.Admin(username, pwd)
        logger.info('管理员%s注册成功' % username)
        return True,'注册成功'

def admin_login_interface(name, password):
    obj = models.Admin.get_obj_by_name(name)
    if obj:
        if obj.pwd == password:
            return True, '登陆成功'
        else:
            return False, '密码不正确'
    else:
        return False, '用户名不存在'