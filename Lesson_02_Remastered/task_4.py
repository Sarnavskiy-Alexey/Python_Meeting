"""
File for task 4
"""


def task_4():
    """
    Вводим с клавиатуры многозначное число
    Необходимо узнать и сказать, последовательность цифр этого числа припросмотре слева направо упорядочена по возрастанию или нет.
    Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет
    """
    number = input('Введите число для проверки: ')
    if not number.isdigit():
        print('Введено не число!')
    else:
        message = f'Цифры числа {number} упорядочены по возрастанию!'
        for i in range(1, len(number)):
            if number[i - 1] >= number[i]:
                message = f'Цифры числа {number} не упорядочены по возрастанию!'
                break
        print(message)


if __name__ == '__main__':
    task_4()