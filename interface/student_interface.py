from db import models

def register_interface(username, pwd):
    student_obj = models.Student.select(username)
    if not student_obj:
        models.Student(username, pwd)
        return True, f'{username}注册成功'

    else:
        return False, f'{username}已经注册'

def choose_school_interface(student_name, school_name):
    student_obj = models.Student.select(student_name)
    if school_name in student_obj.course_list:
        return False, f'{school_name}已经存在'
    student_obj.choose_school(school_name)
    return True, f'{school_name}选择成功'

def choose_course_interface(student_name, school_name, course_name):
    school_obj = models.School.select(school_name)
    if course_name not in school_obj.course_list:
        return False, f'{course_name}不在学校里'

    student_obj = models.Student.select(student_name)
    if course_name in student_obj.course_list:
        return False, f'{course_name}已存在'

    student_obj.choose_course(course_name)

    course_obj = models.Course.select(course_name)
    course_obj.add_student(student_name)
    return True, f'{course_name}添加成功'

def check_score(student_name):
    student_obj = models.Student.select(student_name)
    return student_obj.score


