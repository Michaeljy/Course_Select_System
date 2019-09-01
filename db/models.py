from db import db_handler




class Base:
    @classmethod
    def select(cls, username):
        obj = db_handler.select(cls, username)
        return obj
    def save(self):
        db_handler.save(self)

class Admin(Base):
    def __init__(self, username, pwd):
        self.name = username
        self.pwd = pwd
        self.save()
    def create_school(self, school_name, school_addr):
        School(school_name, school_addr)
    def create_teacher(self, teacher_name, teacher_pwd):
        Teacher(teacher_name, teacher_pwd)
    def create_course(self, course_name, school_name):
        school_obj = School.select(school_name)
        school_obj.create_course(course_name)
        Course(course_name)



class Student(Base):
    def __init__(self, username, pwd):
        self.name = username
        self.pwd = pwd
        self.school = None
        self.course_list = []
        self.score = {}
        self.save()
    def choose_school(self,school_name):
        self.school = school_name
        self.save()
    def choose_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

class Teacher(Base):
    def __init__(self, username, pwd):
        self.name = username
        self.pwd = pwd
        self.course_list = []
        self.save()
    def choose_course(self, course_name):
        self.course_list.append(course_name)
        self.save()
    def check_student(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.student_list
    def change_score(self, course_name, student_name, score):
        student_obj = Student.select(student_name)
        student_obj.score[course_name] = score
        student_obj.save()

class School(Base):
    def __init__(self, school_name, school_addr):
        self.name = school_name
        self.pwd = school_addr
        self.course_list = []
        self.save()
    def create_course(self, course_name):
        self.course_list.append(course_name)
        self.save()


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name
        self.student_list = []
        self.save()
    def add_student(self, student_name):
        self.student_list.append(student_name)
        self.save()
