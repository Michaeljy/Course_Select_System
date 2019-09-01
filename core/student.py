from conf import settings
from lib import common
from interface import student_interface, common_interface

student_info = {
    'user': None
}


def student_register():
    while True:
        print('欢迎来到学生注册界面')

        username = input('请输入姓名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        flag, msg = student_interface.register_interface(username, pwd)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


def student_login():
    while True:
        print("欢迎来到学生登录界面")
        username = input('请输入姓名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        flag, msg = common_interface.login_interface(
            username, pwd, 'student')
        if flag:
            print(msg)
            student_info['user'] = username
            break
        else:
            print(msg)
            break


@common.login_auth('student')
def choose_school():
    while True:
        print('欢迎来到选择学校界面')

        school_list = common_interface.get_school_list()
        for k, v in enumerate(school_list):
            print(f'{k} {v}')

        school_choice = input('请选择学校,或按q退出>>>').strip()
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
        flag, msg = student_interface.choose_school_interface(
            student_info['user'], school_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth('student')
def choose_course():
    while True:
        print('欢迎来到选择课程界面')
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
        course_list = common_interface.get_course_list()
        for k, v in enumerate(course_list):
            print(f'{k} {v}')

        course_choice = input('请选择课程,或q退出>>>').strip()
        if course_choice == 'q':
            break
        if not course_choice.isdigit():
            print('请输入数字')
            continue
        course_choice = int(course_choice)
        if course_choice not in range(len(course_list)):
            print('请输入正确的数字')
            continue
        course_name = course_list[course_choice]
        flag,msg = student_interface.choose_course_interface(
            student_info['user'], school_name, course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth('student')
def check_score():
    while True:
        print("欢迎来到查看分数界面")

        msg = student_interface.check_score(student_info['user'])
        print(msg)
        break


student_dic = {
    '1': student_register,
    '2': choose_school,
    '3': choose_school,
    '4': choose_course,
    '5': check_score
}


def student():
    while True:
        print(settings.STUDENT_MSG)
        func_choice = input('请选择视图，或q退出>>>').strip()
        if func_choice == 'q':
            break
        func = student_dic[func_choice]
        if not func:
            print("输入有误！")
            continue
        func()
