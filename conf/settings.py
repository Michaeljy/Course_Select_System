import os



CSS2_PATH = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(CSS2_PATH, 'db')

FUNC_MSG = '''
    1.管理员视图
    2.学生视图
    3.教师视图
'''
ADMIN_MSG = '''
    1.注册
    2.登录
    3.创建学校
    4.创建教师
    5.创建课程
'''
STUDENT_MSG = '''
    1.注册
    2.登录
    3.选择学校
    4.选择课程
    5.查看成绩
'''
TEACHER_MSG = '''
    1.登录
    2.查看课程
    3.选择课程
    4.查看课程学生
    5.修改成绩
'''