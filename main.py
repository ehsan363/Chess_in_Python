table = [['brl', 'bhl', 'bbl', 'bq', 'bk', 'bbr', 'bhr', 'brr'],
         ['bp0', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['wp0', 'wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7'],
         ['wrl', 'whl', 'wbl', 'wq', 'wk', 'wbr', 'whr', 'wrr']]
chance = 'white'
one = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def change_changer(ch):
    if ch == 'white':
        global change
        change = 'black'
    elif ch == 'black':
        change = 'white'


pos = [['brl'], ['bhl'], ['bbl'], ['bq'], ['bk'], ['bbr'], ['bhr'], ['brr'],
       ['bp0'], ['bp1'], ['bp2'], ['bp3'], ['bp4'], ['bp5'], ['bp6'], ['bp7'],
       ['wp0'], ['wp1'], ['wp2'], ['wp3'], ['wp4'], ['wp5'], ['wp6'], ['wp7'],
       ['wrl'], ['whl'], ['wbl'], ['wq'], ['wk'], ['wbr'], ['whr'], ['wrr']]


def valid_pos(chance):
    if chance == 'white':
        for i in range(len(table)):
            for j in range(len(table[i])):

                if table[i][j][0] == 'w':
                    if table[i][j][1] == 'p':
                        for piece in range(len(pos)):
                            if pos[piece][0] == table[i][j]:
                                if one[int(table[i][j][2]) + 8] == 1 and table[i - 2][j] == '0':
                                    pos[piece].append((j, i - 2))
                                    one[int(table[i][j][2]) + 8] = 0
                                if table[i - 1][j] == '0':
                                    pos[piece].append((j, i - 1))
                                if j != 0:
                                    if table[i - 1][j - 1][0] == 'b':
                                        pos[piece].append((j - 1, i - 1))
                                if j != 7:
                                    if table[i - 1][j - 1][0] == 'b':
                                        pos[piece].append((j + 1, i - 1))

                    if table[i][j][1] == 'r':
                        if table[i][j][2] == 'r':
                            piece = pos[31]
                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j):
                                            if table[i][l][0] == 'w':
                                                break
                                            if table[i][l][0] == '0':
                                                piece.append((l, i))
                                            elif table[i][l][0] == 'b':
                                                piece.append((l, i))
                                                break

                                elif move == 1:
                                    if i != 0:
                                        for u in range(i - 1, -1, -1):
                                            if table[u][j][0] == 'w':
                                                break
                                            if table[u][j][0] == '0':
                                                print((u, j), '(u, j) #2')
                                                print(table[u][j], 'did it!')
                                                piece.append((j, u))
                                            elif table[u][j][0] == 'b':
                                                piece.append((j, u))
                                                break

                                elif move == 2:
                                    if j != 7:
                                        for r in range(j + 1, 8):
                                            if table[i][r][0] == 'w':
                                                break
                                            if table[i][r][0] == '0':
                                                piece.append((r, i))
                                            elif table[i][r][0] == 'b':
                                                piece.append((r, i))
                                                break
                                elif move == 3:
                                    if i != 7:
                                        for d in range(i + 1, 8):
                                            if table[d][j][0] == 'w':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'b':
                                                piece.append((j, d))
                                                break

                        if table[i][j][2] == 'l':
                            piece = pos[24]
                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j):
                                            if table[i][l][0] == 'w':
                                                break
                                            if table[i][l][0] == '0':
                                                piece.append((l, i))
                                            elif table[i][l][0] == 'b':
                                                piece.append((l, i))
                                                break

                                elif move == 1:
                                    if i != 0:
                                        for u in range(i - 1, -1, -1):
                                            if table[u][j][0] == 'w':
                                                break
                                            if table[u][j][0] == '0':
                                                piece.append((j, u))
                                            elif table[u][j][0] == 'b':
                                                piece.append((j, u))
                                                break

                                elif move == 2:
                                    if j != 7:
                                        for r in range(j + 1, 8):
                                            if table[i][r][0] == 'w':
                                                break
                                            if table[i][r][0] == '0':
                                                piece.append((r, i))
                                            elif table[i][r][0] == 'b':
                                                piece.append((r, i))
                                                break
                                elif move == 3:
                                    if i != 7:
                                        for d in range(i + 1, 8):
                                            print(table[i][l])
                                            if table[d][j][0] == 'w':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'b':
                                                piece.append((j, d))










    elif chance == 'black':
        print()

    print(pos)
    print('####################################')
    cm = 0
    for i in pos:
        if len(i) != 1:
            cm += (len(i) - 1)
    print(cm)


valid_pos(chance)