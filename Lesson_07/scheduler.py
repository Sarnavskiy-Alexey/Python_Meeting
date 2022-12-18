"""
File with task 1
"""

import task_1_show_data as T1SD
import task_1_change_data as T1CD
import task_1_add_data as T1AD

GL_filename = 'scheduler.txt'
menu = """1 - для вывода на экран необходимой информации;
2 - для изменения записанных данных;
3 - для добавления новых данных;
4 - для показа данного меню;
0 - для выхода"""


def scheduler():
    """Запуск планировщика"""
    print("""\nВас приветствует планировщик занятий на GeekBrains!
Чтобы работать с планировщиком, нажимайте необходимые клавиши!"""
)
    while(1):
        print(menu)
        answer = int(input('Выберите действие 1, 2, 3, 4, 0: '))
        print()
        if answer == 0: break
        elif answer == 1: T1SD.show_data(GL_filename)
        elif answer == 2: T1CD.change_data(GL_filename)
        elif answer == 3: T1AD.add_data(GL_filename)
        elif answer == 4: print(menu)
        print()
    print()
    print('До свидания!')


if __name__ == '__main__':
    scheduler()
