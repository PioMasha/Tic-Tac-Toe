PLAYER_SYMBOLS = ".0X"
ROW_INDICES = "ABC"
COLUMN_INDICES = "123"


def welcome_game():
    """
        Приветствует игроков
        :return:
        """
    print("Добро пожаловать в игру крестики-нолики!")


welcome_game()
game_field = [[0 for _ in range(3)] for _ in range(3)]


def print_game_field(gf):
    """
        Создаёт и возвращает поле для игры в виде двумерного списка
        :param PLAYER_SYMBOLS: символ игрока
        :param row: ряд игрового поля
        :param cell: ячейка игрового поля
        :return: вывод игрового поля на экран
        """
    for row in gf:
        for cell in row:
            print(PLAYER_SYMBOLS[cell], end=" ")
        print()


def is_tie(gf):
    """
        Проверяет заполнено ли поле полностью для определения результата "ничья"
        :param row: ряд игрового поля
        :return: возвращает True, если строки заполнены иначе False
        """
    return all(map(lambda row: all(row), gf))


def is_completed(gf):
    """
        Определяет конечный результат игры и какой игрок выиграл
        :param j: столбцы игрового поля
        :param i: элемент игрового поля
        :param inv_diagonal, diagonal: диагонали игрового поля
        :return: вызывает фун-ю "ничья" для проверки
        """
    for row in gf:
        cell1, cell2, cell3 = row
        if (cell1 == cell2 == cell3) and cell1 != 0:
            return True, cell1

    for j in range(len(gf[0])):
        first = gf[0][j]
        if first != 0:
            for i in range(1, len(gf)):
                if gf[i][j] != first:
                    break
            else:
                return True, first

    diagonal = gf[0][0]
    if diagonal != 0:
        for i in range(len(gf)):
            if gf[i][i] != diagonal:
                break
        else:
            return True, diagonal

    inv_diagonal = gf[0][len(gf) - 1]
    if inv_diagonal != 0:
        for i in range(len(gf)):
            if gf[i][len(gf) - i - 1] != inv_diagonal:
                break
        else:
            return True, inv_diagonal

    return is_tie(gf), 0


current_player = 1
completed, who_win = False, 0


def play_in_game():
    """
        Запрос хода у игроков, определение текущего игрока
        :param current_player: текущий игрок
        :param player_input ввод игроков позиции на поле
        :return: сообщает о победе или о ничье, выводя номер игрока
        """
    global current_player
    global completed, who_win

    while not completed:
        print_game_field(game_field)

        player_input = input(f"Игрок №{current_player}, введите позицию на игровом поле: ")
        if len(player_input) != 2:
            print(
                'Неверное кол-во символов. Введите в формате: А1, где первый символ - ряд из A,B,C, второй - столбец из'
                '1,2,3')
            continue
        player_row, player_column = player_input
        player_row = ROW_INDICES.find(player_row)
        if player_row == -1:
            print("Неверный номер ряда. Укажите ряд:", ",".join(ROW_INDICES))
            continue
        player_column = COLUMN_INDICES.find(player_column)
        if player_column == -1:
            print("Неверный номер строки. Укажите цифру:", ",".join(COLUMN_INDICES))
            continue
        if game_field[player_row][player_column] > 0:
            print("Эта ячейка уже занята. Выберите другую")
            continue
        game_field[player_row][player_column] = current_player

        completed, who_win = is_completed(game_field)

        if current_player == 1:
            current_player = 2
        elif current_player == 2:
            current_player = 1
        else:
            print("Неверный номер игрока")

    if who_win != 0:
        print(f"Игрок №{who_win} победил!")
    else:
        print("Игра завершилась ничьей")

    return who_win


play_in_game()
