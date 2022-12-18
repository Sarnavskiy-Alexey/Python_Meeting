"""
File for get_data methods
"""


def get_data(filename: str) -> list:
    arr_data = []
    with open(filename, 'rt', encoding='UTF-8') as f:
        arr_data = f.readlines()
    for i in range(len(arr_data)):
        if len(arr_data[i]) > 2:
            arr_data[i] = arr_data[i].split(' | ')
            arr_data[i][4] = arr_data[i][4].replace('\n', '')
    return arr_data


def get_new_data() -> list:
    new_date = input('Введите дату и время в формате "dd-mm-yyyy hh:mm" - ')
    new_course = input('Введите название курса - ')
    new_lesson_number = input('Введите номер урока - ')
    new_lesson_theme = input('Введите тему урока - ')
    new_note = input('Введите заметку об уроке - ')
    return [new_date, new_course, new_lesson_number, new_lesson_theme, new_note]
