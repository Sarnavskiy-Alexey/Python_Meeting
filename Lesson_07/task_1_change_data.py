"""
File with change_data methods
"""

from task_1_get_data import get_data, get_new_data
from task_1_print_data import print_data
from task_1_write_data import write_data
from datetime import datetime


def find_relevant_data(data: list, finder: str) -> list:
    res = []
    for item in data:
        for el in item:
            if finder in el:
                res += [item]
                break
    res.sort(key=lambda x: datetime.strptime(x[0], "%d-%m-%Y %H:%M"))
    return res


def find_records_in_data(data) -> list:
    print('Введите текст для поиска записи:')
    answer = input()
    return find_relevant_data(data, answer)


def change_data(filename):
    arr_data = get_data(filename)
    result_find = find_records_in_data(arr_data)

    print_data(result_find)
    idx = 0
    if len(result_find) == 0:
        return
    elif len(result_find) > 1:
        print('По вашему запросу я нашел несколько записей!')
        while idx not in range(1, len(result_find) + 1):
            idx = int(input('Введите номер записи, которую необходимо изменить: '))
    else:
        idx = 1

    if idx:
        print('Введите следующие данные для изменения:')
        new_data = get_new_data()

        for index, item in enumerate(arr_data):
            if item == result_find[idx - 1]:
                arr_data[index] = new_data

        write_data(filename, arr_data, 'wt')
