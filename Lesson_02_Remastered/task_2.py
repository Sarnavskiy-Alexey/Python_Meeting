"""
File with task 2
"""


def task_2():
    """
    Вводим с клавиатуры целое число X. Далее вводим Х целых чисел.
    Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.
    """
    X = int(input('Введите количество чисел: '))
    if X < 1:
        print('Введено неверное количество!')
    else:
        maximum, prev_max = 0, 0
        for i in range(X):
            number = int(input(f'Введите {i + 1}е число: '))
            if not i:
                maximum = number
                if X == 1:
                    prev_max = number
                else:
                    prev_max = '-inf'
            else:
                if number > maximum:
                    prev_max = maximum
                    maximum = number
                elif prev_max == '-inf' or number > prev_max:
                    prev_max = number
        print(f'Максимальное: {maximum}, второе максимальное: {prev_max}')


if __name__ == '__main__':
    task_2()
