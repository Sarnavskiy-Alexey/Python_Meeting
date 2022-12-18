"""
File with print_data methods
"""


from datetime import datetime


def print_data(data):
    today = datetime.today()
    if len(data):
        print('Вот, что я нашел по вашему запросу:')
        for idx, item in enumerate(data, 1):
            print(f'{idx}. {item[0][:10]} в {item[0][11:]} у вас '
                  f'{"было" if datetime.strptime(item[0], "%d-%m-%Y %H:%M") < today else "будет"} '
                  f'{item[2]}е занятие по курсу "{item[1]}" по теме: '
                  f'"{item[3]}".'
                  f'{f""" Вы оставили следующую заметку: "{item[4]}" """ if len(item[4]) else ""}')
    else:
        print('К сожалению, я не нашел нужной информации!')