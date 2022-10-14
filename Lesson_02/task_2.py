"""
File with task 2
"""

def task_2():
    """
    Напишите программу, которая принимает на вход число N
    и выдает набор произведений чисел от 1 до N.
    1-1*1, 2-1*2, 3-1*2*3, 4-1*2*3*4 и т.д.
    """
    print(task_2.__name__)
    N = int(input('Введите целое число N > 0: '))
    if N > 0:
        mult = 1
        for i in range(1, N + 1):
            mult *= i
            print(mult, end='')
            if i != N:
                print(', ', end='')
        print('')
    else:
        print('Вы ввели неправильное число N!')
    print('----------------')
