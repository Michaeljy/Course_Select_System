from db import models

def register_interface(username, pwd):
    admin_obj = models.Admin.select(username)
    if not admin_obj:
        models.Admin(username, pwd)
        return True, f'{username}注册成功'

    else:
        return False, f'{username}已经注册'

def create_school_interface(username, school_name, school_addr):
    admin_obj = models.Admin.select(username)
    school_obj = models.School.select(school_name)
    if school_obj:
        return False, f'{school_name}已经存在'
    admin_obj.create_school(school_name, school_addr)
    return True, f'{school_name}创建成功'

def create_teacher_interface(username, teacher_name, teacher_pwd = '123'):
    admin_obj = models.Admin.select(username)
    teacher_obj = models.Teacher.select(teacher_name)
    if teacher_obj:
        return False, f'{teacher_name}已经存在'
    admin_obj.create_teacher(teacher_name, teacher_pwd)
    return True, f'{teacher_name}创建成功'
def create_course_interface(username, course_name,school_name):# 创建课程时要把课程加到学校的列表里
    admin_obj = models.Admin.select(username)
    school_obj = models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False, f'{course_name}已经存在'
    admin_obj.create_course(course_name, school_name)
    return True, f'{course_name}创建成功'
