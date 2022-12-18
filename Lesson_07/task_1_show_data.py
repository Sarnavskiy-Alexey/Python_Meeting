"""
File for show_data additional methods
"""
from datetime import datetime
import task_1_print_data as T1PD
from task_1_get_data import get_data


menu = "1 - по датам;\n2 - по курсам;\n3 - по номерам уроков;\n4 - по темам урока;\n5 - по заметкам\n6 - все\n0 - возврат в предыдущее меню"


def find_by_lesson_numbers(data: list) -> list:
    res = []
    answer = int(input('Введите номер урока для поиска: '))
    for item in data:
        if str(answer) == item[2]:
            res += [item]
    res.sort(key=lambda x: int(x[2]))
    return res


def find_by_dates(data: list) -> list:
    res = []
    print('Введите дату в формате "dd-mm-yyyy" или диапазон дат в формате "dd-mm-yyyy":')
    diapason = input()
    first = datetime.strptime(diapason[:10], "%d-%m-%Y")
    second = datetime.strptime(diapason[-10:], "%d-%m-%Y")
    for item in data:
        if first <= datetime.strptime(item[0][:10], "%d-%m-%Y") <= second:
            res += [item]
    res.sort(key=lambda x: datetime.strptime(x[0], "%d-%m-%Y %H:%M"))
    return res


def answer_for_find(idx: int) -> str:
    d = {0: 'дат', 1 : 'курсов', 2 : 'номеров уроков', 3 : 'тем уроков', 4 : 'заметок'}
    print(f'Введите слово, словосочетание или предложение для поиска среди {d[idx]}:')
    return input()


def find_by_text(data: list, answer: str, idx=1) -> list:
    res = []
    for item in data:
        if item[idx].find(answer) != -1:
            res += [item]
    res.sort(key=lambda x: x[idx])
    return res


def show_data(filename: str):
    arr_data = get_data(filename)

    print("Какие данные Вас интересуют?")
    while(1):
        print(menu)
        answer = int(input('Выберите действие: 1, 2, 3, 4, 5, 6, 0: '))
        print()
        if answer == 0: break
        elif answer == 1: T1PD.print_data(find_by_dates(arr_data))
        elif answer == 2: T1PD.print_data(find_by_text(arr_data, answer_for_find(1), 1))
        elif answer == 3: T1PD.print_data(find_by_lesson_numbers(arr_data))
        elif answer == 4: T1PD.print_data(find_by_text(arr_data, answer_for_find(3), 3))
        elif answer == 5: T1PD.print_data(find_by_text(arr_data, answer_for_find(4), 4))
        elif answer == 6: T1PD.print_data(sorted(arr_data, key=lambda x : datetime.strptime(x[0], "%d-%m-%Y %H:%M")))
        print()


if __name__ == '__main__':
    pass
