from db import db_hander
class Admin():
    # 用户的属性
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        self.save()
    def save(self):
        db_hander.save(self)

    @classmethod
    def get_obj_by_name(cls,name):
        return db_hander.select(name,cls.__name__.lower())

class file():
    # 文件的属性
    def __init__(self,fname,ftype):
        self.fname=fname
        self.ftype=ftype
        self.url='',
        self.save()

    def save(self):
        db_hander.save(self)
