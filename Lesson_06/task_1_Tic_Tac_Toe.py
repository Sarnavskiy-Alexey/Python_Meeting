"""
File with task 1
"""

from random import randint

game_field = []


def check_strings_of_gf(gf):
    for el in gf:
        if ' ' not in el:
            if 'O' not in el:
                return 1
            elif 'X' not in el:
                return 2
    return 0


def transpose_matrix(matrix):
    transposed = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            transposed[j][i] = matrix[i][j]
    return transposed


def end_of_game():
    """компаратор на окончание игры"""
    check_end = check_strings_of_gf(game_field)
    if not check_end:
        check_end = check_strings_of_gf(transpose_matrix(game_field))
    if check_end:
        return check_end

    s_tacs_main = 0
    s_toes_main = 0
    s_tacs_back = 0
    s_toes_back = 0
    for i in range(len(game_field)):
        if game_field[i][i] == 'X':
            s_tacs_main += 1
        if game_field[len(game_field) - i - 1][i] == 'X':
            s_tacs_back += 1
        if game_field[i][i] == 'O':
            s_toes_main += 1
        if game_field[len(game_field) - i - 1][i] == 'O':
            s_toes_back += 1
    if s_tacs_main == len(game_field) or s_tacs_back == len(game_field):
        return 1
    elif s_toes_main == len(game_field) or s_toes_back == len(game_field):
        return 2
    else:
        return 0


def beat_by_pos(pos, mark):
    if len(pos) != 2 or pos[0] < 0 or pos[0] >= len(game_field) or pos[1] < 0 or pos[1] >= len(game_field):
        print('Увы вы промахнулись! Ход переходит другому игроку!')
    else:
        if game_field[pos[0]][pos[1]] != ' ':
            print('Увы вы попали в заполненную клетку! Ход переходит другому игроку!')
        else:
            game_field[pos[0]][pos[1]] = mark


def Tic_Tac_Toe(pl1, pl2):
    """Собственно реализация механики игры"""
    turn = 1 if pl1 == 'X' else 2
    the_end = 0
    while not the_end:
        print(f'Ход игрока {turn}!')
        pos = input(f'Введите две координаты для вставки {pl1 if turn == 1 else pl2} (два числа через пробел): ')
        pos = pos.split()
        if len(pos) != 2 or not pos[0].isdigit() or not pos[1].isdigit():
            print('Вы неудачник, который неправильно ввел два числа через пробел! Ход переходит сопернику!')
        else:
            pos[0], pos[1] = int(pos[0]), int(pos[1])
            beat_by_pos(pos, pl1 if turn == 1 else pl2)
            print_field()
        turn = turn % 2 + 1
        the_end = end_of_game()
    print(f'Выиграл игрок {the_end}!')


def print_field():
    """Вывод поля на экран"""
    for els in game_field:
        print(end='| ')
        for el in els:
            print(el, end=' | ')
        print()


def start_game():
    """Инициализация игры Крестики-нолики"""
    print("""Вас приветствует игра "Крестики-нолики"!
Вводимые координаты удара должны быть в пределах от 0 до выбранного размера поля (не включительно).
Выбор игрока, управляющего крестиками, осуществляется автоматически.""")
    global game_field
    field_size = int(input('Введите размер поля: '))
    if field_size <= 2:
        print('Слишком маленькое поле!')
        return
    if field_size > 10:
        print('Слишком большое поле!')
        return
    game_field = [[' ' for _ in range(field_size)] for _ in range(field_size)]
    mark1 = 'X' if randint(1, 2) == 1 else 'O'
    mark2 = 'X' if mark1 == 'O' else 'O'
    print(f'Первый игрок ставит {"крестики" if mark1 == "X" else "нолики"}!')
    print(f'Второй игрок ставит {"крестики" if mark2 == "X" else "нолики"}!')
    print_field()
    Tic_Tac_Toe(mark1, mark2)


if __name__ == '__main__':
    """
    Сделать игру Крестики-нолики
    """
    start_game()
