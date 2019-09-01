from conf import settings
from interface import admin_interface,common_interface
from lib import common

admin_info = {
    'user': None
}

def admin_register():
    while True:
        print('欢迎来到管理员注册界面')

        username = input('请输入姓名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        flag,msg = admin_interface.register_interface(username, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

def admin_login():
    while True:
        print("欢迎来到管理员登录界面")
        username = input('请输入姓名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        flag, msg = common_interface.login_interface(
            username, pwd, 'admin')
        if flag:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)
            break

@common.login_auth('admin')
def create_school():
    while True:
        print('欢迎来到创建学校界面')

        school_name = input('请输入学校名>>>').strip()
        school_addr = input('请输入学校地址>>>').strip()
        flag, msg = admin_interface.create_school_interface(
            admin_info['user'], school_name, school_addr)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

@common.login_auth('admin')
def create_teacher():
    while True:
        print('欢迎来到创建教师界面')
        teacher_name = input('请输入教师名>>>').strip()
        flag, msg,  = admin_interface.create_teacher_interface(
            admin_info['user'], teacher_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

@common.login_auth('admin')
def create_course(): # 创建课程要先选择学校，判断学校的课程列表里面有没有课程
    while True:
        print('欢迎来到创建课程界面')

        school_list = common_interface.get_school_list()
        for k, v in enumerate(school_list):
            print(f'{k} {v}')

        school_choice = input('请选择学校,或q退出>>>').strip()
        if school_choice == 'q':
            break
        if not school_choice.isdigit():
            print('请输入数字')
            continue
        school_choice = int(school_choice)
        if school_choice not in range(len(school_list)):
            print('请输入正确的数字')
            continue
        school_name = school_list[school_choice]
        course_name = input('请输入课程名>>>').strip()
        flag, msg,  = admin_interface.create_course_interface(
            admin_info['user'], course_name,school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

admin_dic = {
    '1': admin_register ,
    '2': admin_login,
    '3': create_school,
    '4': create_teacher,
    '5': create_course
}

def admin():
    while True:
        print(settings.ADMIN_MSG)
        func_choice = input('请选择视图，或q退出>>>').strip()
        if func_choice == 'q':
            break
        func = admin_dic[func_choice]
        if not func:
            print("输入有误！")
            continue
        func()
