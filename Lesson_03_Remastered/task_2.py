"""
File with task 2
"""

def task_2():
    """
    Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом.
    """
    print(task_2.__name__)

    number = input('Введите строку для проверки: ')
    for c in number:
        if not c.isdigit() and c != '.':
            print('Введенная строка вообще не является числом!')
            break
    else:
        print(f'Введенная строка является {"целым" if float(number).is_integer() else "вещественным"} числом.')

    print('----------------')


if __name__ == '__main__':
    task_2()
