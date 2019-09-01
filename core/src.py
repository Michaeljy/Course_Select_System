from core.admin import admin
from core.student import student
from core.teacher import teacher
from conf import settings



func_dic = {
    '1': admin ,
    '2': student,
    '3': teacher,
}

def run():
    while True:
        print('欢迎来到主视图')
        print(settings.FUNC_MSG)
        func_choice = input('请选择视图，或q退出>>>').strip()
        if func_choice == 'q':
            break
        func = func_dic[func_choice]
        if not func:
            print("输入有误！")
            continue
        func()