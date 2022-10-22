"""
File with task 4
"""

from random import randint


def task_4():
    """
    * Задана натуральная степень k. Сформировать случайным образом список коэффициентов
    (от 0 до 10) многочлена, записать в файл полученный многочлен не менее 3-х раз.
    """
    print(task_4.__name__)

    for i in range(3):
        Get_n_Write()

    print('----------------')


def Get_n_Write():
    """
    Функция, выполняющая получение натурального числа k от пользователя, списка с
    рандомными значениями в количестве элементов k, а также выписку получаемого
    многочлена в текстовый файл.
    :return: nothing
    """
    k = int(input('Введите натуральную степень: '))
    l = []
    for i in range(k):
        l.append(randint(0, 10))
    print('Полученный список случайных чисел: ', l)

    for i in range(len(l)):
        if (k - i - 1) != 0:
            if (l[i] != 0):
                l[i] = str(l[i]) + "*x^" + str(k - i - 1) + (" + " if randint(0, 1) else " - ")
            else:
                l[i] = ""

    with open("task_4.txt", "a", encoding="utf-8") as outfile:
        if k > 0:
            outfile.write("".join(map(str, l)) + " = 0\n")
        outfile.close()


if __name__ == '__main__':
    task_4()
