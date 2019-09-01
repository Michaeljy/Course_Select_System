from conf import settings
from lib import common
from interface import teacher_interface, common_interface

teacher_info = {
    'user': None
}

def teacher_login():
    while True:
        print("欢迎来到教师登录界面")
        username = input('请输入姓名>>>').strip()
        pwd = input('请输入密码>>>').strip()
        flag, msg = common_interface.login_interface(
            username, pwd, 'teacher')
        if flag:
            print(msg)
            teacher_info['user'] = username
            break
        else:
            print(msg)
            break

@common.login_auth('teacher')
def check_course():
    while True:
        print("欢迎来到查看课程界面")

        msg = teacher_interface.cheak_course_interface(
            teacher_info['user'])
        print(msg)
        break

@common.login_auth('teacher')
def choose_course():
    while True:
        print("欢迎来到选择课程界面")

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
        flag,msg = teacher_interface.choose_course_interface(
            teacher_info['user'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break

@common.login_auth('teacher')
def check_student():
    while True:
        print("欢迎来到查看课程学生界面")

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
        flag,msg = teacher_interface.check_student(
            teacher_info['user'], course_name)
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


@common.login_auth('teacher')
def change_score():
    while True:
        print("欢迎来到修改成绩界面")
        course_list = teacher_interface.cheak_course_interface(
            teacher_info['user'])
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
        flag, student_list_or_msg = teacher_interface.check_student(
            teacher_info['user'], course_name)
        if flag:
            for k, v in enumerate(student_list_or_msg):
                print(f'{k} {v}')

            student_choice = input('请选择学生,或q退出>>>').strip()
            if student_choice == 'q':
                break
            if not student_choice.isdigit():
                print('请输入数字')
                continue
            student_choice = int(student_choice)
            if student_choice not in range(len(student_list_or_msg)):
                print('请输入正确的数字')
                continue
            student_name = student_list_or_msg[student_choice]
            score = input('请输入成绩，或按q退出>>>').strip()
            if score == 'q':
                break
            msg = teacher_interface.change_score(
                teacher_info['user'], course_name, student_name, score)
            print(msg)
            break
        else:
            print(student_list_or_msg)
            break


teacher_dic = {
    '1': teacher_login ,
    '2': check_course,
    '3': choose_course,
    '4': check_student,
    '5': change_score
}

def teacher():
    while True:
        print("欢迎来到教师视图")
        print(settings.TEACHER_MSG)
        func_choice = input('请选择视图，或q退出>>>').strip()
        if func_choice == 'q':
            break
        func = teacher_dic[func_choice]
        if not func:
            print("输入有误！")
            continue
        func()
