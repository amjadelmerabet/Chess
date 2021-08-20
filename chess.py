P1 = 1
P2 = 2

Player1Tokens = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Player2Tokens = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
P1_index = 0
P2_index = 0

def draw_board(tab):
    for i in range(8):
        if i == 0:
            print('     A     B     C     D     E     F     G     H   ')
        print('  +-----+-----+-----+-----+-----+-----+-----+-----+')
        for j in range(8):
            if j == 0:
                print(i+1,end = ' ')
            if tab[i][j] == 0:
                print('|     ',end = '')
            elif tab[i][j] == 10:
                print('| K1  ',end = '')
            elif tab[i][j] == 20:
                print('| K2  ',end = '')
            elif tab[i][j] == 11:
                print('| Q1  ',end = '')
            elif tab[i][j] == 21:
                print('| Q2  ',end = '')
            elif tab[i][j] == 12:
                print('| H1  ',end = '')
            elif tab[i][j] == 22:
                print('| H2  ',end = '')
            elif tab[i][j] == 13:
                print('| T1  ',end = '')
            elif tab[i][j] == 23:
                print('| T2  ',end = '')
            elif tab[i][j] == 14:
                print('| E1  ',end = '')
            elif tab[i][j] == 24:
                print('| E2  ',end = '')
            elif tab[i][j] == 15:
                print('| Kg1 ',end = '')
            elif tab[i][j] == 25:
                print('| Kg2 ',end = '')
            if j == 7:
                print('|')
    print('  +-----+-----+-----+-----+-----+-----+-----+-----+')

def play(tab,Player,P1_index,P2_index):
    col = ['A','B','C','D','E','F','G','H']
    print("which token you awnt to play")
    x = int(input('Enter the line of your token : '))
    x = x -1
    y = input('Enter the column of your token : ')
    for i in range(8):
        if y == col[i]:
            y = i
    good_way = 0
    good_move = 0
    while good_move == 0:
        if tab[x][y] <= 15 and Player == P1 or tab[x][y] >= 20 and Player == P2:
            l_play = int(input("Enter the line where you want to move this token : "))
            l_play = l_play - 1
            c_play = input("Enter the column where you want to move this token : ")
            for i in range(8):
                if c_play == col[i]:
                    c_play = i

            if tab[x][y] == 10 or tab[x][y] == 20:
                if ((l_play == x+1 or l_play == x-1) and (c_play == y+1 or c_play == y-1 or c_play == y)) or l_play == x and (c_play == y+1 or c_play == y-1):
                    good_way = 1
            if tab[x][y] == 11 or tab[x][y] == 21:
                if (l_play == x and (c_play < 8 and c_play >= 0 and c_play != y) or ((l-play < 8 and l_play >= 0 and l_play != x) and c_play == y)):
                    good_way = 1
                    for i in range(8):
                        if (l_play < 8 and l_play >= 0) and (c_play < 8 and c_play >= 0) and ((l_play == x+i and c_play == y+i) or (l_play == x+i and c_play == y-i) or (l_play == x-i and c_play == y+i) or (l_play == x-i and c_play == y-i)):
                            good_way = 1
            if tab[x][y] == 12 or tab[x][y] == 22:
                if ((l_play == x + 2 or l_play == x-2) and (c_play == y+1 or c_play == y-1)) or ((l_play == x+1 or l_play == x-1) and (c_play == y+2 or c_play == y-2)): 
                    good_way = 1
            if tab[x][y] == 13 or tab[x][y] == 23:
                if ((l_play >= 0 and l_play < 8 and l_play != x) and c_play == y) or (l_play == x and (c_play >= 0 and c_play < 8 and c_play != y)):
                    good_way = 1
            if tab[x][y] == 14 or tab[x][y] == 24:
                for i in range(8):
                    if (l_play < 8 and l_play >= 0) and (c_play < 8 and c_play >= 0) and ((l_play == x+i and c_play == y+i) or (l_play == x+i and c_play == y-i) or (l_play == x-i and c_play == y+i) or (l_play == x-i and c_play == y-i)):
                        good_way = 1
                    good_way = 1
            if tab[x][y] == 15 or tab[x][y] == 25:
                if Player == P1:
                    if x == 6:
                        if (l_play == x-1 or l_play == x-2) and c_play == y:
                            if tab[l_play][c_play] == 0:
                                good_way = 1
                    else:
                        if l_play == x-1 and c_play == y:
                            if tab[l_play][c_play] == 0:
                                good_way = 1
                    if l_play == x-1 and (c_play == y+1 or c_play == y-1) and tab[l_play][c_play] != 0:
                        good_way = 1
             
                if Player == P2:
                    if x == 1:
                        if (l_play == x+1 or l_play == x+2) and c_play == y:
                            if tab[l_play][c_play] == 0:
                                good_way = 1
                    else:
                        if l_play == x+1 and c_play == y:
                            if tab[l_play][c_play] == 0:
                                good_way = 1
                    if l_play == x+1 and (c_play == y+1 or c_play == y-1) and tab[l_play][c_play] != 0:
                        good_way = 1

        if good_way == 1:
            good_move = 1
            if Player == P1:
                if tab[l_play][c_play] == 0 or tab[l_play][c_play] >= 20:
                    if tab[l_play][c_play] != 0:
                        Player2Tokens[P2_index] = tab[l_play][c_play]
                        P2_index = P2_index + 1
                    tab[l_play][c_play] = tab[x][y]
                    tab[x][y] = 0
                else:
                    good_move = 0
                    print("You can't play in that cellule")
            if Player == P2:
                if tab[l_play][c_play] == 0 or tab[l_play][c_play] <= 15:
                    if tab[l_play][c_play] != 0:
                        Player1Tokens[P1_index] = tab[l_play][c_play]
                        P1_index = P1_index + 1
                    tab[l_play][c_play] = tab[x][y]
                    tab[x][y] = 0
                else:
                    good_move = 0
                    print("You can't play in that cellule")
        else:
            print("You can't play in that cellule")

    return tab,P1_index,P2_index

def change_player(Player):
    if Player == P1:
        return P2
    else:
        return P1

def game_over(tab,Player):
    Kings = 0
    for i in range(8):
        for j in range(8):
            if tab[i][j] == 10 or tab[i][j] == 20:
                Kings = Kings + 1
    if Kings < 2:
        return 1
    if Player == P1:
        for i in range(8):
            for j in range(8):
                if tab[i][j] == 10:
                    x = i
                    y = j
        x_play = [x,x+1,x-1]
        y_play = [y,y+1,y-1]
        for i in range(3):
            for j in range(3):
                noway = 0
                if i == 0 and j == 0:
                    pass
                else:
                    for k in range(x_play[i],8):
                        if tab[k][y_play[j]] == 23 or tab[k][y_play[j]] == 21:
                            noway = 1
                    for k in range(0,x_play[i]):
                        if tab[k][y_play[j]] == 23 or tab[k][y_play[j]] == 21:
                            noway = 1
                    for k in range(y_play[j],8):
                        if tab[x_play[i]][k] == 23 or tab[x_play[i]][k] == 21:
                            noway = 1
                    for k in range(0,y_play[j]):
                        if tab[x_play[i]][k] == 23 or tab[x_play[i]][k] == 21:
                            noway = 1
                    for k in range(8):
                        if x_play[i] + k < 8 and y_play[j] + k < 8:
                            if tab[x_play[i]+k][y_play[j]+k] == 24:
                                noway = 1
                        if x_play[i] + k < 8 and y_play[j] - k >= 0:
                            if tab[x_play[i]+k][y_play[j]-k] == 24:
                                noway = 1
                        if x_play[i] - k >= 0 and y_play[j] + k < 8:
                            if tab[x_play[i]-k][y_play[j]+k] == 24:
                                noway = 1
                        if x_play[i] - k >= 0 and y_play[j] - k >= 0:
                            if tab[x_play[i]-k][y_play[j]-k] == 24:
                                noway = 1
                    if x_play[i] + 3 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]+3][y_play[j]+1] == 22:
                            noway = 1
                    if x_play[i] + 3 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]+3][y_play[j]-1] == 22:
                            noway = 1
                    if x_play[i] - 3 >= 0 and y_play[j] + 1 < 8:
                        if tab[x_play[i]-3][y_play[j]+1] == 22:
                            noway = 1
                    if x_play[i] - 3 >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]-3][y_play[j]-1] == 22:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 3 < 8:
                        if tab[x_play[i]+1][y_play[j]+3] == 22:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]-1][y_play[j]-3] == 22:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]+1][y_play[j]-3] == 22:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]-1][y_play[j]-3] == 22:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] < 8 and y_play[j] >= 0:
                        if tab[x_play[i]+1][y_play[j]] == 20:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]+1][y_play[j]+1] == 20:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]+1][y_play[j]-1] == 20:
                            noway = 1
                    if x_play[i] < 8 and x_play[i] >= 0 and y_play[j] + 1 >= 0:
                        if tab[x_play[i]][y_play[j]+1] == 20:
                            noway = 1
                    if x_play[i] < 8 and x_play[i] >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]][y_play[j]-1] == 20:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] < 8 and y_play[j] >= 0:
                        if tab[x_play[i]-1][y_play[j]] == 20:
                            noay = 1
                    if x_play[i] - 1 >= 0 and y_play[j] + 1 < 8:
                        if tab[x_play[i]-1][y_play[j]+1] == 20:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]-1][y_play[j]-1] == 20:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]+1][y_play[j]+1] == 25:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]+1][y_play[j]-1] == 25:
                            noway = 1 
            if noway == 0:
                return 0
        return 1
    else:
        for i in range(8):
            for j in range(8):
                if tab[i][j] == 20:
                    x = i
                    y = j
        x_play = [x,x+1,x-1]
        y_play = [y,y+1,y-1]
        for i in range(3):
            for j in range(3):
                noway = 0
                if i == 0 and j == 0:
                    pass 
                else:
                    for k in range(x_play[i],8):
                        if tab[k][y_play[j]] == 13 or tab[k][y_play[j]] == 11:
                            noway = 1
                    for k in range(0,x_play[i]):
                        if tab[k][y_play[j]] == 13 or tab[k][y_play[j]] == 11:
                            noway = 1
                    for k in range(y_play[j],8):
                        if tab[x_play[i]][k] == 13 or tab[x_play[i]][k] == 11:
                            noway = 1
                    for k in range(0,y_play[j]):
                        if tab[x_play[i]][k] == 13 or tab[x_play[i]][k] == 11:
                            noway = 1
                    for k in range(8):
                        if x_play[i] + k < 8 and y_play[j] + k < 8:
                            if tab[x_play[i]+k][y_play[j]+k] == 14:
                                noway = 1
                        if x_play[i] + k < 8 and y_play[j] - k >= 0:
                            if tab[x_play[i]+k][y_play[j]-k] == 14:
                                noway = 1
                        if x_play[i] - k >= 0 and y_play[j] + k < 8:
                            if tab[x_play[i]-k][y_play[j]+k] == 14:
                                noway = 1
                        if x_play[i] - k >= 0 and y_play[j] - k >= 0:
                            if tab[x_play[i]-k][y_play[j]-k] == 14:
                                noway = 1
                    if x_play[i] + 3 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]+3][y_play[j]+1] == 12:
                            noway = 1
                    if x_play[i] + 3 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]+3][y_play[j]-1] == 12:
                            noway = 1
                    if x_play[i] - 3 >= 0 and y_play[j] + 1 < 8:
                        if tab[x_play[i]-3][y_play[j]+1] == 12:
                            noway = 1
                    if x_play[i] - 3 >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]-3][y_play[j]-1] == 12:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 3 < 8:
                        if tab[x_play[i]+1][y_play[j]+3] == 12:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]-1][y_play[j]-3] == 12:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]+1][y_play[j]-3] == 12:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 3 >= 0:
                        if tab[x_play[i]-1][y_play[j]-3] == 12:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] < 8 and y_play[j] >= 0:
                        if tab[x_play[i]+1][y_play[j]] == 10:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]+1][y_play[j]+1] == 10:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]+1][y_play[j]-1] == 10:
                            noway = 1
                    if x_play[i] < 8 and x_play[i] >= 0 and y_play[j] + 1 >= 0:
                        if tab[x_play[i]][y_play[j]+1] == 10:
                            noway = 1
                    if x_play[i] < 8 and x_play[i] >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]][y_play[j]-1] == 10:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] < 8 and y_play[j] >= 0:
                        if tab[x_play[i]-1][y_play[j]] == 10:
                            noay = 1
                    if x_play[i] - 1 >= 0 and y_play[j] + 1 < 8:
                        if tab[x_play[i]-1][y_play[j]+1] == 10:
                            noway = 1
                    if x_play[i] - 1 >= 0 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]-1][y_play[j]-1] == 10:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] + 1 < 8:
                        if tab[x_play[i]-1][y_play[j]+1] == 15:
                            noway = 1
                    if x_play[i] + 1 < 8 and y_play[j] - 1 >= 0:
                        if tab[x_play[i]-1][y_play[j]-1] == 15:
                            noway = 1 
            if noway == 0:
                return 0
        return 1

    

Board = [[23,24,22,20,21,22,24,23],[25,25,25,25,25,25,25,25],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[15,15,15,15,15,15,15,15],[13,14,12,11,10,12,14,13]]
Player = P1

gameOver = game_over(Board,Player)

while(gameOver == 0):
    draw_board(Board)
    if Player == P1:
        print("Player 1 turn")
    else:
        print("Player 2 turn")
    Board,P1_index,P2_index = play(Board,Player,P1_index,P2_index)
    print("Player 1 dead tokens : ",end = '')
    for i in range(16):
        if Player1Tokens[i] != 0:
            print(Player1Tokens[i],end = ' ')
    print("")
    print("Player 2 dead tokens : ",end = '')
    for i in range(16):
        if Player2Tokens[i] != 0:
            print(Player2Tokens[i],end = ' ')
    print("")
    gameOver = game_over(Board,Player)
    Player = change_player(Player)



# King = K 10 20
# Queen = Q 11 21
# Horse = H 12 22
# Tower = T 13 23
# Elephant = E 14 24 
# Kgnight = Kg 15 25
 
