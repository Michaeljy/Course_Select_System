from db import models
import os
from conf import settings

def login_interface(username, pwd, type):
    if type == 'admin':
        obj = models.Admin.select(username)
    elif type == 'student':
        obj = models.Student.select(username)
    elif type == 'teacher':
        obj = models.Teacher.select(username)
    else:
        return False, '权限不足'

    if not obj:
        return False, "用户不存在"
    else:
        if obj.pwd == pwd:
            return True, f'{username}登录成功'
        else:
            return False, '密码输入有误'

def get_school_list():
    school_list_dir = os.path.join(
        settings.DB_PATH, 'School')
    if os.path.isdir(school_list_dir):
        school_list = os.listdir(school_list_dir)
        return school_list

def get_course_list():
    course_list_dir = os.path.join(
        settings.DB_PATH, 'Course')
    if os.path.isdir(course_list_dir):
        course_list = os.listdir(course_list_dir)
        return course_list
