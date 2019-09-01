
def login_auth(type):
    def auth(func):
        from core import admin, student, teacher
        def inner(*args, **kwargs):
            if type == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.admin_login()
            if type == 'student':
                if student.student_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    student.student_login()
            if type == 'teacher':
                if teacher.teacher_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    teacher.teacher_login()
        return inner
    return auth