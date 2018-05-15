import re
import sys

board = [
    [5,5,5],
    [5,5,5],
    [5,5,5]
]
player = 1
i=0


def inf_out (board):

    st = str(board)

    st = re.sub('[[,\]]', '', st)
    st = re.sub(' ', '|', st)
    st = re.sub('0', 'O', st)
    st = re.sub('1', 'X', st)
    st = re.sub('5', ' ', st)

    print(st[0:5:1])
    print(st[6:11:1])
    print(st[12:17:1])

def win(board):
    if     ((board[0][0] + board[0][1] + board[0][2]) == 3 or
            (board[1][0] + board[1][1] + board[1][2]) == 3 or
            (board[2][0] + board[2][1] + board[2][2]) == 3 or
            (board[0][0] + board[1][0] + board[2][0]) == 3 or
            (board[0][1] + board[1][1] + board[2][1]) == 3 or
            (board[0][2] + board[1][2] + board[2][2]) == 3 or
            (board[0][0] + board[1][1] + board[2][2]) == 3 or
            (board[2][0] + board[1][1] + board[0][2]) == 3):

         return 1

    elif   ((board[0][0] + board[0][1] + board[0][2]) == 0 or
            (board[1][0] + board[1][1] + board[1][2]) == 0 or
            (board[2][0] + board[2][1] + board[2][2]) == 0 or
            (board[0][0] + board[1][0] + board[2][0]) == 0 or
            (board[0][1] + board[1][1] + board[2][1]) == 0 or
            (board[0][2] + board[1][2] + board[2][2]) == 0 or
            (board[0][0] + board[1][1] + board[2][2]) == 0 or
            (board[2][0] + board[1][1] + board[0][2]) == 0):

        return 0


def cont_geme():
    cont = input("Играть заново? Y/N\n", )
    cont = cont.upper()
    while True:
        if cont == "Y":
            print()
            break

        elif cont == "N":
            sys.exit()

        else:
            print("Введите Y-да или N-нет.")
            continue

while True:
    while i<9 :

        inf_out(board)

        if player:
            print("Первый игрок 'X'")
            fishka = 1
            player= False

        else:
            print("Второй игрок 'O'")
            fishka = 0
            player = True

        while True:

            while True:
                try:
                    x = int(input("Введите строку->")) - 1
                    if x > -1 and x < 3:
                        break
                    else:
                        print("Введите число от 1 до 3:")
                        continue
                except:
                    print("Вы ввели не число. Повторите попытку:")
                    continue

            while True:
                try:
                    y = int(input("Ввeдите столбик->")) - 1
                    if y > -1 and y < 3:
                        break
                    else:
                        print("Введите число от 1 до 3:")
                        continue
                except:
                    print("Вы ввели не число. Повторите попытку:")
                    continue

            if board[x][y] == 5:
                board[x][y] = fishka
                break
            else:
                if board[x][y] == 1:
                    print("На этом месте стоит 'X'. Повторите попытку:")
                    continue
                else:
                    print("На этом месте стоит 'O'. Повторите попытку:")
                    continue

        i += 1
        if win(board)==1:

            print()
            print("Победил первый игрок.")
            inf_out(board)
            cont_geme()
            board = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ]
            player = 1
            i = 0

        elif win(board)==0:

            print()
            print("Победил второй игрок.")
            inf_out(board)
            cont_geme()
            board = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ]
            player = 1
            i = 0


    print()
    print("Ничья.")
    inf_out(board)
    cont_geme()
    board = [
    [5,5,5],
    [5,5,5],
    [5,5,5]
]
    player = 1
    i=0