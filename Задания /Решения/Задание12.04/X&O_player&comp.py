import re
import sys
import random
import time

board = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]
i = 0
end = 0

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
    if     ((board[0][0] + board[0][1] + board[0][2]) == victoryPlayer or
            (board[1][0] + board[1][1] + board[1][2]) == victoryPlayer or
            (board[2][0] + board[2][1] + board[2][2]) == victoryPlayer or
            (board[0][0] + board[1][0] + board[2][0]) == victoryPlayer or
            (board[0][1] + board[1][1] + board[2][1]) == victoryPlayer or
            (board[0][2] + board[1][2] + board[2][2]) == victoryPlayer or
            (board[0][0] + board[1][1] + board[2][2]) == victoryPlayer or
            (board[2][0] + board[1][1] + board[0][2]) == victoryPlayer):

         return 1

    elif   ((board[0][0] + board[0][1] + board[0][2]) == victoryComp or
            (board[1][0] + board[1][1] + board[1][2]) == victoryComp or
            (board[2][0] + board[2][1] + board[2][2]) == victoryComp or
            (board[0][0] + board[1][0] + board[2][0]) == victoryComp or
            (board[0][1] + board[1][1] + board[2][1]) == victoryComp or
            (board[0][2] + board[1][2] + board[2][2]) == victoryComp or
            (board[0][0] + board[1][1] + board[2][2]) == victoryComp or
            (board[2][0] + board[1][1] + board[0][2]) == victoryComp):

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

def logic_comp (board):
    if (board[0][0] + board[0][1] + board[0][2]) == summaWin :
        for i in range(3):
            if board[0][0+i] == 5:
                board[0][0+i] = fishkaComp
                break
            else:
                if board[0][0+i] == fishkaPlayer:
                    continue

    elif (board[1][0] + board[1][1] + board[1][2]) == summaWin :
        for i in range(3):
            if board[1][0+i] == 5:
                board[1][0+i] = fishkaComp
                break
            else:
                if board[1][0+i] == fishkaPlayer:
                    continue

    elif (board[2][0] + board[2][1] + board[2][2]) == summaWin :
        for i in range(3):
            if board[2][0+i] == 5:
                board[2][0+i] = fishkaComp
                break
            else:
                if board[2][0+i] == fishkaPlayer:
                    continue

    elif (board[0][0] + board[1][0] + board[2][0]) == summaWin :
        for i in range(3):
            if board[0+i][0] == 5:
                board[0+i][0] = fishkaComp
                break
            else:
                if board[0+i][0] == fishkaPlayer:
                    continue

    elif (board[0][1] + board[1][1] + board[2][1]) == summaWin :
        for i in range(3):
            if board[0+i][1] == 5:
                board[0+i][1] = fishkaComp
                break
            else:
                if board[0+i][1] == fishkaPlayer:
                    continue

    elif (board[0][2] + board[1][2] + board[2][2]) == summaWin :
        for i in range(3):
            if board[0+i][2] == 5:
                board[0+i][2] = fishkaComp
                break
            else:
                if board[0+i][2] == fishkaPlayer:
                    continue

    elif (board[0][0] + board[1][1] + board[2][2]) == summaWin :

        if board[0][0] == 5:
            board[0][0] = fishkaComp
        elif board[1][1] == 5:
            board[1][1] = fishkaComp
        elif board[2][2] == 5:
            board[2][2] = fishkaComp

    elif (board[0][2] + board[1][1] + board[2][0]) == summaWin :

        if board[0][2] == 5:
            board[0][2] = fishkaComp
        elif board[1][1] == 5:
            board[1][1] = fishkaComp
        elif board[2][0] == 5:
            board[2][0] = fishkaComp

    elif (board[0][0] + board[0][1] + board[0][2]) == summaLose :
        for i in range(3):
            if board[0][0+i] == 5:
                board[0][0+i] = fishkaComp
                break
            else:
                if board[0][0+i] == fishkaPlayer:
                    continue

    elif (board[1][0] + board[1][1] + board[1][2]) == summaLose :
        for i in range(3):
            if board[1][0+i] == 5:
                board[1][0+i] = fishkaComp
                break
            else:
                if board[1][0+i] == fishkaPlayer:
                    continue

    elif (board[2][0] + board[2][1] + board[2][2]) == summaLose :
        for i in range(3):
            if board[2][0+i] == 5:
                board[2][0+i] = fishkaComp
                break
            else:
                if board[2][0+i] == fishkaPlayer:
                    continue

    elif (board[0][0] + board[1][0] + board[2][0]) == summaLose :
        for i in range(3):
            if board[0+i][0] == 5:
                board[0+i][0] = fishkaComp
                break
            else:
                if board[0+i][0] == fishkaPlayer:
                    continue

    elif (board[0][1] + board[1][1] + board[2][1]) == summaLose :
        for i in range(3):
            if board[0+i][1] == 5:
                board[0+i][1] = fishkaComp
                break
            else:
                if board[0+i][1] == fishkaPlayer:
                    continue

    elif (board[0][2] + board[1][2] + board[2][2]) == summaLose :
        for i in range(3):
            if board[0+i][2] == 5:
                board[0+i][2] = fishkaComp
                break
            else:
                if board[0+i][2] == fishkaPlayer:
                    continue

    elif (board[0][0] + board[1][1] + board[2][2]) == summaLose :

        if board[0][0] == 5:
            board[0][0] = fishkaComp
        elif board[1][1] == 5:
            board[1][1] = fishkaComp
        elif board[2][2] == 5:
            board[2][2] = fishkaComp

    elif (board[0][2] + board[1][1] + board[2][0]) == summaLose :

        if board[0][2] == 5:
            board[0][2] = fishkaComp
        elif board[1][1] == 5:
            board[1][1] = fishkaComp
        elif board[2][0] == 5:
            board[2][0] = fishkaComp

    else:
        while True:
            x=random.randrange(0, 3, 1)
            y=random.randrange(0, 3, 1)
            if board[x][y] == 5 :
                board[x][y] = fishkaComp
                break
            else:
                continue

def logic_player():
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
                board[x][y] = fishkaPlayer
                break
            else:
                if board[x][y] == 1:
                    print("На этом месте стоит 'X'. Повторите попытку:")
                    continue
                else:
                    print("На этом месте стоит 'O'. Повторите попытку:")
                    continue


while True:
    print("Вы хотите играть первым или вторым?")
    while True:
        try:
            turn = int(input("Введите 1 или 2\n"))
            if turn == 1:
                fishkaPlayer = 1
                fishkaComp = 0
                summaLose = 7
                summaWin = 5
                victoryPlayer = 3
                victoryComp = 0
                player = True
                break
            elif turn == 2:
                fishkaPlayer = 0
                fishkaComp = 1
                summaLose = 5
                summaWin = 7
                victoryPlayer = 0
                victoryComp = 3
                player = False
                break
            else:
                continue
        except:
            print("Вы ввели не число")

    while True :
        if end :
            break

        inf_out(board)

        if player:
            print("Игрок:")
            logic_player()
            player= False

        else:
            print("Компьютер:")
            time.sleep(2)
            logic_comp(board)
            player = True
        i += 1
        print(i)

        if win(board)==1:

            print()
            print("Победил игрок.")
            inf_out(board)
            cont_geme()
            board = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ]
            i = 0
            break

        elif win(board)==0:

            print()
            print("Победил компьютер.")
            inf_out(board)
            cont_geme()
            board = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ]
            i = 0
            break

        if i == 9:
            print()
            print("Ничья.")
            inf_out(board)
            cont_geme()
            end = 1
            board = [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]
            ]
            i = 0

