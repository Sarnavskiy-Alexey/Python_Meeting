"""
File for show_data additional methods
"""
from datetime import datetime
import Lesson_10.scheduler.scheduler_print_data as SPD
from Lesson_10.scheduler.scheduler_get_data import get_data


menu = "1 - по датам;\n2 - по курсам;\n3 - по номерам уроков;\n4 - по темам урока;\n5 - по заметкам\n6 - все\n0 - возврат в предыдущее меню"


def find_by_lesson_numbers(data: list, answer: str) -> list:
    res = []
    for item in data:
        if answer == item[2]:
            res += [item]
    res.sort(key=lambda x: int(x[2]))
    return res


def find_by_dates(data: list, dates: str) -> list:
    res = []
    first = datetime.strptime(dates[:10], "%d-%m-%Y")
    second = datetime.strptime(dates[-10:], "%d-%m-%Y")
    for item in data:
        if first <= datetime.strptime(item[0][:10], "%d-%m-%Y") <= second:
            res += [item]
    res.sort(key=lambda x: datetime.strptime(x[0], "%d-%m-%Y %H:%M"))
    return res


def find_by_text(data: list, answer: str, idx=1) -> list:
    res = []
    for item in data:
        if item[idx].find(answer) != -1:
            res += [item]
    res.sort(key=lambda x: x[idx])
    return res


def show_data(mes: list[str]) -> str:
    arr_data = get_data('scheduler\\scheduler.txt')

    if len(mes):
        if mes[0].lower() == 'дата':
            return SPD.print_data(find_by_dates(arr_data, mes[1]))
        elif mes[0].lower() == 'курс':
            return SPD.print_data(find_by_text(arr_data, mes[1], 1))
        elif mes[0].lower() == 'урок':
            return SPD.print_data(find_by_lesson_numbers(arr_data, mes[1]))
        elif mes[0].lower() == 'тема':
            return SPD.print_data(find_by_text(arr_data, mes[1], 3))
        elif mes[0].lower() == 'заметка':
            return SPD.print_data(find_by_text(arr_data, mes[1], 4))
        else:
            return 'Такой тег отсутствует!'
    else:
        return SPD.print_data(sorted(arr_data, key=lambda x: datetime.strptime(x[0], "%d-%m-%Y %H:%M")))


if __name__ == '__main__':
    pass
