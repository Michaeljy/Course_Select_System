from db import models


def cheak_course_interface(teacher_name):
    teacher_obj = models.Teacher.select(teacher_name)
    return teacher_obj.course_list

def choose_course_interface(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)

    if course_name in teacher_obj.course_list:
        return False, f'{course_name}已经存在'
    teacher_obj.choose_course(course_name)
    return True, f'{course_name}选择成功'

def check_student(teacher_name, course_name):
    teacher_obj = models.Teacher.select(teacher_name)
    if course_name not in teacher_obj.course_list:
        return False, f'{course_name}未找到'

    student_list = teacher_obj.check_student(course_name)
    return True, student_list

def change_score(teacher_name, course_name, student_name, score):
    teacher_obj = models.Teacher.select(teacher_name)
    teacher_obj.change_score(course_name, student_name, score)
    return f'{course_name}成绩修改成功'