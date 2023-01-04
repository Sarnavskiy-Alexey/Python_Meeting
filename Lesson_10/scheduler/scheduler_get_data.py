"""
File for get_data methods
"""

from Lesson_10.scheduler.scheduler_write_data import write_data


def get_data(filename: str) -> list:
    arr_data = []
    with open(filename, 'rt', encoding='UTF-8') as f:
        arr_data = f.readlines()
    for i in range(len(arr_data)):
        if len(arr_data[i]) > 2:
            arr_data[i] = arr_data[i].split(' | ')
            arr_data[i][4] = arr_data[i][4].replace('\n', '')
    return arr_data


def get_new_data(mes: list[str]):
    new_date = mes[0]
    new_course = mes[1]
    new_lesson_number = mes[2]
    new_lesson_theme = mes[3]
    new_note = mes[4]
    write_data('scheduler\\scheduler.txt', [[new_date, new_course, new_lesson_number, new_lesson_theme, new_note]], 'at')
