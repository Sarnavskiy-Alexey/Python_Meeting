"""
File with task 5
"""

import random


def task_5():
    """
    Даны два файла, в каждом из которых находится запись многочленов.
    Задача - сформировать файл, содержащий сумму многочленов.
    """
    print(task_5.__name__)

    str_file1 = str(input('Введите название первого файла: '))
    str_file2 = str(input('Введите название второго файла: '))

    if count_lines(str_file1) == count_lines(str_file2):
        with open(str_file1, "r") as infile_1:
            with open(str_file2, "r") as infile_2:
                outfile = open("task_5_ready.txt", "w", encoding="utf-8")
                for i in range(count_lines(str_file1)):
                    outfile.write(edit_strings(infile_1.readline(), infile_2.readline()))
                outfile.close()
    else:
        print('Количество строк с многочленами в файлах - разное!')

    print('----------------')


def count_lines(filename):
    return sum(1 for line in open(filename, "r"))


def edit_strings(str_1, str_2) -> str:
    return str_1.replace(" = 0\n", " + " + str_2, 1)


if __name__ == '__main__':
    task_5()
