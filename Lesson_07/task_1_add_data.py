"""
File with add_data methods
"""

from task_1_get_data import get_new_data
from task_1_write_data import write_data


def add_data(filename):
    print('Введите новые данные для добавления в расписание')
    new_data = get_new_data()
    write_data(filename, [new_data], 'at')
