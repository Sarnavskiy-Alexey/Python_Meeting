"""
File with task 1
"""

def task_1():
    """
    Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
    """
    print(task_1.__name__)

    source_number = int(input('Введите десятичное число для перевода: '))
    number, sign = abs(source_number), ('-0x' if source_number < 0 else '0x')
    res = ''
    while number > 15:
        mod = number % 16
        res = ('A' if mod == 10\
            else 'B' if mod == 11\
            else 'C' if mod == 12\
            else 'D' if mod == 13\
            else 'E' if mod == 14\
            else 'F' if mod == 15\
            else str(mod)) + res
        number = number // 16
    res = sign + str(number) + res
    print(f'Число {source_number} в 16-ричном представлении: {res}')

    print('----------------')


if __name__ == '__main__':
    task_1()
