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
pure = [1, 1, 1, 1, 1, 1]


def chance_changer(ch):
    if ch == 'white':
        global chance
        chance = 'black'
    elif ch == 'black':
        chance = 'white'


pos = [['brl'], ['bhl'], ['bbl'], ['bq'], ['bk'], ['bbr'], ['bhr'], ['brr'],
       ['bp0'], ['bp1'], ['bp2'], ['bp3'], ['bp4'], ['bp5'], ['bp6'], ['bp7'],
       ['wp0'], ['wp1'], ['wp2'], ['wp3'], ['wp4'], ['wp5'], ['wp6'], ['wp7'],
       ['wrl'], ['whl'], ['wbl'], ['wq'], ['wk'], ['wbr'], ['whr'], ['wrr']]


def distance(m, ii, jj):
    global dis
    dis = 0
    if m == 0:
        if ii > 7 - jj:
            dis = 7 - jj
        elif 7 - jj > ii:
            dis = ii
        elif 7 - jj == ii:
            dis = ii

    elif m == 1:
        if 7 - jj > 7 - ii:
            dis = 7 - ii
        elif 7 - ii > 7 - jj:
            dis = 7 - jj
        elif 7 - ii == 7 - jj:
            dis = 7 - ii
    elif m == 2:
        if jj > 7 - ii:
            dis = 7 - ii
        elif 7 - ii > jj:
            dis = jj
        elif 7 - ii == jj:
            dis = jj

    elif m == 3:
        if ii > jj:
            dis = jj
        elif jj > ii:
            dis = ii
        elif jj == ii:
            dis = ii


def valid_pos(chance):
    if chance == 'white':
        for i in range(len(table)):
            for j in range(len(table[i])):

                if table[i][j][0] == 'w':
                    if table[i][j][1] == 'p':

                        for piece in pos:
                            if piece[0] == table[i][j]:
                                if one[int(table[i][j][2]) + 8] == 1 and table[i - 1][j] == '0' and table[i - 2][
                                    j] == '0':
                                    piece.append((j, i - 1))
                                    piece.append((j, i - 2))
                                elif one[int(table[i][j][2]) + 8] == 0 and table[i - 1][j] == '0':
                                    piece.append((j, i - 1))
                                if j != 0 and i != 0:

                                    if table[i - 1][j - 1][0] == 'b':
                                        piece.append((j - 1, i - 1))
                                    if table[i - 1][j - 1][0] == 'b' and one[int(table[i][j - 1][2])] == 2:
                                        piece.append((j - 1, i - 1))

                                if j != 7 and i != 0:
                                    if table[i - 1][j + 1][0] == 'b':
                                        piece.append((j + 1, i - 1))
                                    if table[i - 1][j + 1][0] == 'b' and one[int(table[i][j + 1][2])] == 2:
                                        piece.append((j + 1, i - 1))

                        if i == 6:
                            one[int(table[i][j][2]) + 8] = 1
                        elif i == 5:
                            one[int(table[i][j][2]) + 8] = 0
                        elif i == 4 and one[int(table[i][j][2])] == 0:
                            one[int(table[i][j][2]) + 8] = 2
                        elif i == 3:
                            one[int(table[i][j][2]) + 8] = 0

                    if table[i][j][1] == 'r':
                        if table[i][j][2] == 'r':
                            piece = pos[31]

                            if i != 7 or j != 7:
                                pure[5] = 0

                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j - 1, -1, -1):
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
                                            if table[d][j][0] == 'w':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'b':
                                                piece.append((j, d))
                                                break

                        if table[i][j][2] == 'l':
                            piece = pos[24]

                            if i != 7 or j != 0:
                                pure[3] = 0

                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j - 1, -1, -1):
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
                                            if table[d][j][0] == 'w':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'b':
                                                piece.append((j, d))
                                                break

                    if table[i][j][1] == 'h':
                        if table[i][j][2] == 'l':
                            piece = pos[25]
                            if i != 0 and i != 1 and j != 0:
                                if table[i - 2][j - 1][0] != 'w':
                                    piece.append((j - 1, i - 2))
                            if j != 0 and j != 1 and i != 0:
                                if table[i - 1][j - 2][0] != 'w':
                                    piece.append((j - 2, i - 1))
                            if i != 0 and i != 1 and j != 7:
                                if table[i - 2][j + 1][0] != 'w':
                                    piece.append((j + 1, i - 2))
                            if j != 7 and j != 6 and i != 0:
                                if table[i - 1][j + 2][0] != 'w':
                                    piece.append((j + 2, i - 1))
                            if i != 7 and i != 6 and j != 7:
                                if table[i + 2][j + 1][0] != 'w':
                                    piece.append((j + 1, i + 2))
                            if j != 7 and j != 6 and i != 7:
                                if table[i + 1][j + 2][0] != 'w':
                                    piece.append((j + 2, i + 1))
                            if i != 7 and i != 6 and j != 0:
                                if table[i + 2][j - 1][0] != 'w':
                                    piece.append((j - 1, i + 2))
                            if j != 0 and j != 1 and i != 7:
                                if table[i + 1][j - 2][0] != 'w':
                                    piece.append((j - 2, i + 1))

                        elif table[i][j][2] == 'r':
                            piece = pos[30]

                            if i != 0 and i != 1 and j != 0:
                                if table[i - 2][j - 1][0] != 'w':
                                    piece.append((j - 1, i - 2))
                            if j != 0 and j != 1 and i != 0:
                                if table[i - 1][j - 2][0] != 'w':
                                    piece.append((j - 2, i - 1))
                            if i != 0 and i != 1 and j != 7:
                                if table[i - 2][j + 1][0] != 'w':
                                    piece.append((j + 1, i - 2))
                            if j != 7 and j != 6 and i != 0:
                                if table[i - 1][j + 2][0] != 'w':
                                    piece.append((j + 2, i - 1))
                            if i != 7 and i != 6 and j != 7:
                                if table[i + 2][j + 1][0] != 'w':
                                    piece.append((j + 1, i + 2))
                            if j != 7 and j != 6 and i != 7:
                                if table[i + 1][j + 2][0] != 'w':
                                    piece.append((j + 2, i + 1))
                            if i != 7 and i != 6 and j != 0:
                                if table[i + 2][j - 1][0] != 'w':
                                    piece.append((j - 1, i + 2))
                            if j != 0 and j != 1 and i != 7:
                                if table[i + 1][j - 2][0] != 'w':
                                    piece.append((j - 2, i + 1))

                    if table[i][j][1] == 'b':
                        if table[i][j][2] == 'l':
                            piece = pos[26]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move, i, j)
                                        for ur in range(1, dis + 1):
                                            if table[i - ur][j + ur][0] == 'w':
                                                break
                                            if table[i - ur][j + ur][0] == '0':
                                                piece.append((j + ur, i - ur))
                                            elif table[i - ur][j + ur][0] == 'b':
                                                piece.append((j + ur, i - ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move, i, j)
                                        for dr in range(1, dis + 1):
                                            if table[i + dr][j + dr][0] == 'w':
                                                break
                                            elif table[i + dr][j + dr][0] == '0':
                                                piece.append((j + dr, i + dr))
                                            elif table[i + dr][j + dr][0] == 'b':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move, i, j)
                                        for dl in range(1, dis + 1):
                                            if table[i + dl][j - dl][0] == 'w':
                                                break
                                            elif table[i + dl][j - dl][0] == '0':
                                                piece.append((j - dl, i + dl))
                                            elif table[i + dl][j - dl][0] == 'b':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move, i, j)
                                        for ul in range(1, dis + 1):
                                            if table[i - ul][j - ul][0] == 'w':
                                                break
                                            elif table[i - ul][j - ul][0] == '0':
                                                piece.append((j - ul, i - ul))
                                            elif table[i - ul][j - ul][0] == 'b':
                                                piece.append((j - ul, i - ul))
                                                break


                        elif table[i][j][2] == 'r':
                            piece = pos[29]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move, i, j)
                                        for ur in range(1, dis + 1):
                                            if table[i - ur][j + ur][0] == 'w':
                                                break
                                            if table[i - ur][j + ur][0] == '0':
                                                piece.append((j + ur, i - ur))
                                            elif table[i - ur][j + ur][0] == 'b':
                                                piece.append((j + ur, i - ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move, i, j)
                                        for dr in range(1, dis + 1):
                                            if table[i + dr][j + dr][0] == 'w':
                                                break
                                            elif table[i + dr][j + dr][0] == '0':
                                                piece.append((j + dr, i + dr))
                                            elif table[i + dr][j + dr][0] == 'b':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move, i, j)
                                        for dl in range(1, dis + 1):
                                            if table[i + dl][j - dl][0] == 'w':
                                                break
                                            elif table[i + dl][j - dl][0] == '0':
                                                piece.append((j - dl, i + dl))
                                            elif table[i + dl][j - dl][0] == 'b':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move, i, j)
                                        for ul in range(1, dis + 1):
                                            if table[i - ul][j - ul][0] == 'w':
                                                break
                                            elif table[i - ul][j - ul][0] == '0':
                                                piece.append((j - ul, i - ul))
                                            elif table[i - ul][j - ul][0] == 'b':
                                                piece.append((j - ul, i - ul))
                                                break
                    if table[i][j][1] == 'k':
                        piece = pos[28]
                        if pure[4] == 1 and pure[5] == 1:
                            if table[i][j + 1] == '0' and table[i][j + 2] == '0':
                                av1 = 1
                                av2 = 1
                                for b in pos:
                                    if b[0][0] == 'b':
                                        if (j + 1, i) in b:
                                            av1 -= 1
                                        if (j + 2, i) in b:
                                            av2 -= 1
                                if av1 == 1 and av2 == 1:
                                    piece.append((j + 3, i))

                        if j != 4 or i != 7:
                            pure[4] = 1

                        if pure[4] == 1 and pure[3] == 1:
                            if table[i][j - 1] == '0' and table[i][j - 2] == '0' and table[i][j - 3] == '0':
                                av1 = 1
                                av2 = 1
                                av3 = 1
                                for b in pos:
                                    if b[0][0] == 'b':
                                        if (j - 1, i) in b:
                                            av1 -= 1
                                        if (j - 2, i) in b:
                                            av2 -= 1
                                        if (j - 3, i) in b:
                                            av3 -= 1
                                if av1 == 1 and av2 == 1 and av3 == 1:
                                    piece.append((j - 4, i))

                        if i != 0:
                            if table[i - 1][j][0] != 'w':
                                piece.append((j, i - 1))
                        if i != 0 and j != 0:
                            if table[i - 1][j - 1][0] != 'w':
                                piece.append((j - 1, i - 1))
                        if j != 0:
                            if table[i][j - 1][0] != 'w':
                                piece.append((j - 1, i))
                        if j != 0 and i != 7:
                            if table[i + 1][j - 1][0] != 'w':
                                piece.append((j - 1, i + 1))
                        if i != 7:
                            if table[i + 1][j][0] != 'w':
                                piece.append((j, i + 1))
                        if i != 7 and j != 7:
                            if table[i + 1][j + 1][0] != 'w':
                                piece.append((j + 1, i + 1))
                        if j != 7:
                            if table[i][j + 1][0] != 'w':
                                piece.append((j + 1, i))

                    if table[i][j][1] == 'q':
                        piece = pos[27]
                        for move in range(8):

                            if move == 0:
                                if j != 0:
                                    for l in range(j - 1, -1, -1):
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
                                        if table[d][j][0] == 'w':
                                            break
                                        if table[d][j][0] == '0':
                                            piece.append((j, d))
                                        elif table[d][j][0] == 'b':
                                            piece.append((j, d))
                                            break

                            elif move == 4:
                                if j != 7 and i != 0:
                                    distance(0, i, j)
                                    for ur in range(1, dis + 1):
                                        if table[i - ur][j + ur][0] == 'w':
                                            break
                                        if table[i - ur][j + ur][0] == '0':
                                            piece.append((j + ur, i - ur))
                                        elif table[i - ur][j + ur][0] == 'b':
                                            piece.append((j + ur, i - ur))
                                            break


                            elif move == 5:
                                if j != 7 and i != 7:
                                    distance(1, i, j)
                                    for dr in range(1, dis + 1):
                                        if table[i + dr][j + dr][0] == 'w':
                                            break
                                        elif table[i + dr][j + dr][0] == '0':
                                            piece.append((j + dr, i + dr))
                                        elif table[i + dr][j + dr][0] == 'b':
                                            piece.append((j + dr, i + dr))
                                            break

                            elif move == 6:
                                if j != 0 and i != 7:
                                    distance(2, i, j)
                                    for dl in range(1, dis + 1):
                                        if table[i + dl][j - dl][0] == 'w':
                                            break
                                        elif table[i + dl][j - dl][0] == '0':
                                            piece.append((j - dl, i + dl))
                                        elif table[i + dl][j - dl][0] == 'b':
                                            piece.append((j - dl, i + dl))
                                            break

                            elif move == 7:
                                if j != 0 and i != 0:
                                    distance(3, i, j)
                                    for ul in range(1, dis + 1):
                                        if table[i - ul][j - ul][0] == 'w':
                                            break
                                        elif table[i - ul][j - ul][0] == '0':
                                            piece.append((j - ul, i - ul))
                                        elif table[i - ul][j - ul][0] == 'b':
                                            piece.append((j - ul, i - ul))
                                            break


                elif table[i][j][0] == 'b':
                    if table[i][j][1] == 'p':
                        for piece in pos:
                            if piece[0] == table[i][j]:
                                if one[int(table[i][j][2])] == 1 and table[i - 1][j] == '0' and table[i - 2][j] == '0':
                                    piece.append((j, i + 1))
                                    piece.append((j, i + 2))
                                elif one[int(table[i][j][2])] == 1 and table[i - 1][j] == '0' and table[i - 2][
                                    j] != '0':
                                    piece.append((j, i + 1))
                                elif one[int(table[i][j][2])] == 0 and table[i - 1][j] == '0':
                                    piece.append((j, i + 1))

                                if j != 0 and i != 7:
                                    if table[i + 1][j - 1][0] == 'w':
                                        piece.append((j - 1, i + 1))
                                    if table[i][j - 1][0] == 'b' and one[int(table[i][j - 1][2]) + 8] == 2:
                                        piece.append((j - 1, i + 1))

                                if j != 7 and i != 7:
                                    if table[i + 1][j + 1][0] == 'w':
                                        piece.append((j + 1, i + 1))
                                    if table[i][j + 1][0] == 'w' and one[int(table[i][j + 1][2]) + 8] == 2:
                                        piece.append((j + 1, i + 1))

                    if table[i][j][1] == 'r':
                        if table[i][j][2] == 'r':
                            piece = pos[7]

                            if i != 0 or j != 7:
                                pure[0] = 0

                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j - 1, -1, -1):
                                            if table[i][l][0] == 'b':
                                                break
                                            if table[i][l][0] == '0':
                                                piece.append((l, i))
                                            elif table[i][l][0] == 'w':
                                                piece.append((l, i))
                                                break

                                elif move == 1:
                                    if i != 0:
                                        for u in range(i - 1, -1, -1):
                                            if table[u][j][0] == 'b':
                                                break
                                            if table[u][j][0] == '0':
                                                piece.append((j, u))
                                            elif table[u][j][0] == 'w':
                                                piece.append((j, u))
                                                break

                                elif move == 2:
                                    if j != 7:
                                        for r in range(j + 1, 8):
                                            if table[i][r][0] == 'b':
                                                break
                                            if table[i][r][0] == '0':
                                                piece.append((r, i))
                                            elif table[i][r][0] == 'w':
                                                piece.append((r, i))
                                                break
                                elif move == 3:
                                    if i != 7:
                                        for d in range(i + 1, 8):
                                            if table[d][j][0] == 'b':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'w':
                                                piece.append((j, d))
                                                break

                        if table[i][j][2] == 'l':
                            piece = pos[0]

                            if i != 0 or j != 0:
                                pure[2] = 0

                            for move in range(4):

                                if move == 0:
                                    if j != 0:
                                        for l in range(j - 1, -1, -1):
                                            if table[i][l][0] == 'b':
                                                break
                                            if table[i][l][0] == '0':
                                                piece.append((l, i))
                                            elif table[i][l][0] == 'w':
                                                piece.append((l, i))
                                                break

                                elif move == 1:
                                    if i != 0:
                                        for u in range(i - 1, -1, -1):
                                            if table[u][j][0] == 'b':
                                                break
                                            if table[u][j][0] == '0':
                                                piece.append((j, u))
                                            elif table[u][j][0] == 'w':
                                                piece.append((j, u))
                                                break

                                elif move == 2:
                                    if j != 7:
                                        for r in range(j + 1, 8):
                                            if table[i][r][0] == 'b':
                                                break
                                            if table[i][r][0] == '0':
                                                piece.append((r, i))
                                            elif table[i][r][0] == 'w':
                                                piece.append((r, i))
                                                break
                                elif move == 3:
                                    if i != 7:
                                        for d in range(i + 1, 8):
                                            if table[d][j][0] == 'b':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'w':
                                                piece.append((j, d))
                                                break

                    if table[i][j][1] == 'h':
                        if table[i][j][2] == 'l':
                            piece = pos[1]
                            if i != 0 and i != 1 and j != 0:
                                if table[i - 2][j - 1][0] != 'b':
                                    piece.append((j - 1, i - 2))
                            if j != 0 and j != 1 and i != 0:
                                if table[i - 1][j - 2][0] != 'b':
                                    piece.append((j - 2, i - 1))
                            if i != 0 and i != 1 and j != 7:
                                if table[i - 2][j + 1][0] != 'b':
                                    piece.append((j + 1, i - 2))
                            if j != 7 and j != 6 and i != 0:
                                if table[i - 1][j + 2][0] != 'b':
                                    piece.append((j + 2, i - 1))
                            if i != 7 and i != 6 and j != 7:
                                if table[i + 2][j + 1][0] != 'b':
                                    piece.append((j + 1, i + 2))
                            if j != 7 and j != 6 and i != 7:
                                if table[i + 1][j + 2][0] != 'b':
                                    piece.append((j + 2, i + 1))
                            if i != 7 and i != 6 and j != 0:
                                if table[i + 2][j - 1][0] != 'b':
                                    piece.append((j - 1, i + 2))
                            if j != 0 and j != 1 and i != 7:
                                if table[i + 1][j - 2][0] != 'b':
                                    piece.append((j - 2, i + 1))

                        elif table[i][j][2] == 'r':
                            piece = pos[6]

                            if i != 0 and i != 1 and j != 0:
                                if table[i - 2][j - 1][0] != 'b':
                                    piece.append((j - 1, i - 2))
                            if j != 0 and j != 1 and i != 0:
                                if table[i - 1][j - 2][0] != 'b':
                                    piece.append((j - 2, i - 1))
                            if i != 0 and i != 1 and j != 7:
                                if table[i - 2][j + 1][0] != 'b':
                                    piece.append((j + 1, i - 2))
                            if j != 7 and j != 6 and i != 0:
                                if table[i - 1][j + 2][0] != 'b':
                                    piece.append((j + 2, i - 1))
                            if i != 7 and i != 6 and j != 7:
                                if table[i + 2][j + 1][0] != 'b':
                                    piece.append((j + 1, i + 2))
                            if j != 7 and j != 6 and i != 7:
                                if table[i + 1][j + 2][0] != 'b':
                                    piece.append((j + 2, i + 1))
                            if i != 7 and i != 6 and j != 0:
                                if table[i + 2][j - 1][0] != 'b':
                                    piece.append((j - 1, i + 2))
                            if j != 0 and j != 1 and i != 7:
                                if table[i + 1][j - 2][0] != 'b':
                                    piece.append((j - 2, i + 1))

                    if table[i][j][1] == 'b':
                        if table[i][j][2] == 'l':
                            piece = pos[2]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move, i, j)
                                        for ur in range(1, dis + 1):
                                            if table[i - ur][j + ur][0] == 'b':
                                                break
                                            if table[i - ur][j + ur][0] == '0':
                                                piece.append((j + ur, i - ur))
                                            elif table[i - ur][j + ur][0] == 'w':
                                                piece.append((j + ur, i - ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move, i, j)
                                        for dr in range(1, dis + 1):
                                            if table[i + dr][j + dr][0] == 'b':
                                                break
                                            elif table[i + dr][j + dr][0] == '0':
                                                piece.append((j + dr, i + dr))
                                            elif table[i + dr][j + dr][0] == 'w':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move, i, j)
                                        for dl in range(1, dis + 1):
                                            if table[i + dl][j - dl][0] == 'b':
                                                break
                                            elif table[i + dl][j - dl][0] == '0':
                                                piece.append((j - dl, i + dl))
                                            elif table[i + dl][j - dl][0] == 'w':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move, i, j)
                                        for ul in range(1, dis + 1):
                                            if table[i - ul][j - ul][0] == 'b':
                                                break
                                            elif table[i - ul][j - ul][0] == '0':
                                                piece.append((j - ul, i - ul))
                                            elif table[i - ul][j - ul][0] == 'w':
                                                piece.append((j - ul, i - ul))
                                                break


                        elif table[i][j][2] == 'r':
                            piece = pos[5]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move, i, j)
                                        for ur in range(1, dis + 1):
                                            if table[i - ur][j + ur][0] == 'b':
                                                break
                                            if table[i - ur][j + ur][0] == '0':
                                                piece.append((j + ur, i - ur))
                                            elif table[i - ur][j + ur][0] == 'w':
                                                piece.append((j + ur, i - ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move, i, j)
                                        for dr in range(1, dis + 1):
                                            if table[i + dr][j + dr][0] == 'b':
                                                break
                                            elif table[i + dr][j + dr][0] == '0':
                                                piece.append((j + dr, i + dr))
                                            elif table[i + dr][j + dr][0] == 'w':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move, i, j)
                                        for dl in range(1, dis + 1):
                                            if table[i + dl][j - dl][0] == 'b':
                                                break
                                            elif table[i + dl][j - dl][0] == '0':
                                                piece.append((j - dl, i + dl))
                                            elif table[i + dl][j - dl][0] == 'w':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move, i, j)
                                        for ul in range(1, dis + 1):
                                            if table[i - ul][j - ul][0] == 'b':
                                                break
                                            elif table[i - ul][j - ul][0] == '0':
                                                piece.append((j - ul, i - ul))
                                            elif table[i - ul][j - ul][0] == 'w':
                                                piece.append((j - ul, i - ul))
                                                break

                    if table[i][j][1] == 'k':

                        piece = pos[4]
                        if pure[1] == 1 and pure[2] == 1:
                            if table[i][j + 1] == '0' and table[i][j + 2] == '0':
                                av1 = 1
                                av2 = 1
                                for w in pos:
                                    if w[0][0] == 'w':
                                        if (j + 1, i) in w:
                                            av1 -= 1
                                        if (j + 2, i) in w:
                                            av2 -= 1
                                if av1 == 1 and av2 == 1:
                                    piece.append((j + 3, i))

                        if pure[1] == 1 and pure[0] == 1:
                            if table[i][j - 1] == '0' and table[i][j - 2] == '0' and table[i][j - 3] == '0':
                                av1 = 1
                                av2 = 1
                                av3 = 1
                                for w in pos:
                                    if w[0][0] == 'w':
                                        if (j - 1, i) in w:
                                            av1 -= 1
                                        if (j - 2, i) in w:
                                            av2 -= 1
                                        if (j - 3, i) in w:
                                            av3 -= 1
                                if av1 == 1 and av2 == 1 and av3 == 1:
                                    piece.append((j - 4, i))

                        if j != 4 or i != 0:
                            pure[1] = 0

                        if i != 0:
                            if table[i - 1][j][0] != 'b':
                                piece.append((j, i - 1))
                        if i != 0 and j != 0:
                            if table[i - 1][j - 1][0] != 'b':
                                piece.append((j - 1, i - 1))
                        if j != 0:
                            if table[i][j - 1][0] != 'b':
                                piece.append((j - 1, i))
                        if j != 0 and i != 7:
                            if table[i + 1][j - 1][0] != 'b':
                                piece.append((j - 1, i + 1))
                        if i != 7:
                            if table[i + 1][j][0] != 'b':
                                piece.append((j, i + 1))
                        if i != 7 and j != 7:
                            if table[i + 1][j + 1][0] != 'b':
                                piece.append((j + 1, i + 1))
                        if j != 7:
                            if table[i][j + 1][0] != 'b':
                                piece.append((j + 1, i))

                    if table[i][j][1] == 'q':
                        piece = pos[3]
                        for move in range(8):

                            if move == 0:
                                if j != 0:
                                    for l in range(j - 1, -1, -1):
                                        if table[i][l][0] == 'b':
                                            break
                                        if table[i][l][0] == '0':
                                            piece.append((l, i))
                                        elif table[i][l][0] == 'w':
                                            piece.append((l, i))
                                            break

                            elif move == 1:
                                if i != 0:
                                    for u in range(i - 1, -1, -1):
                                        if table[u][j][0] == 'b':
                                            break
                                        if table[u][j][0] == '0':
                                            piece.append((j, u))
                                        elif table[u][j][0] == 'w':
                                            piece.append((j, u))
                                            break

                            elif move == 2:
                                if j != 7:
                                    for r in range(j + 1, 8):
                                        if table[i][r][0] == 'b':
                                            break
                                        if table[i][r][0] == '0':
                                            piece.append((r, i))
                                        elif table[i][r][0] == 'w':
                                            piece.append((r, i))
                                            break
                            elif move == 3:
                                if i != 7:
                                    for d in range(i + 1, 8):
                                        if table[d][j][0] == 'b':
                                            break
                                        if table[d][j][0] == '0':
                                            piece.append((j, d))
                                        elif table[d][j][0] == 'w':
                                            piece.append((j, d))
                                            break

                            elif move == 4:
                                if j != 7 and i != 0:
                                    distance(0, i, j)
                                    for ur in range(1, dis + 1):
                                        if table[i - ur][j + ur][0] == 'b':
                                            break
                                        if table[i - ur][j + ur][0] == '0':
                                            piece.append((j + ur, i - ur))
                                        elif table[i - ur][j + ur][0] == 'w':
                                            piece.append((j + ur, i - ur))
                                            break


                            elif move == 5:
                                if j != 7 and i != 7:
                                    distance(1, i, j)
                                    for dr in range(1, dis + 1):
                                        if table[i + dr][j + dr][0] == 'b':
                                            break
                                        elif table[i + dr][j + dr][0] == '0':
                                            piece.append((j + dr, i + dr))
                                        elif table[i + dr][j + dr][0] == 'w':
                                            piece.append((j + dr, i + dr))
                                            break

                            elif move == 6:
                                if j != 0 and i != 7:
                                    distance(2, i, j)
                                    for dl in range(1, dis + 1):
                                        if table[i + dl][j - dl][0] == 'b':
                                            break
                                        elif table[i + dl][j - dl][0] == '0':
                                            piece.append((j - dl, i + dl))
                                        elif table[i + dl][j - dl][0] == 'w':
                                            piece.append((j - dl, i + dl))
                                            break

                            elif move == 7:
                                if j != 0 and i != 0:
                                    distance(3, i, j)
                                    for ul in range(1, dis + 1):
                                        if table[i - ul][j - ul][0] == 'b':
                                            break
                                        elif table[i - ul][j - ul][0] == '0':
                                            piece.append((j - ul, i - ul))
                                        elif table[i - ul][j - ul][0] == 'w':
                                            piece.append((j - ul, i - ul))
                                            break


def validpos_filter(mode, attacker):
    def filtering(os):
        if os == 'b':
            global kpiece, side
            kpiece = pos[28]
            side = 'w'
        elif os == 'w':
            kpiece = pos[4]
            side = 'b'
        for i in pos:
            if i[0][0] == os:
                for j in i:
                    if j in kpiece:
                        kpiece.remove(j)

        global beam
        beam = []
        oneshot = list('hkp')
        if attacker[0] == os and attacker[1] == 'r':
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j][0] == os and table[i][j][1] == 'r':
                        attacker_pos = [j, i]
                        aj = j
                        ai = i
                    elif table[i][j][0] == side and table[i][j][1] == 'k':
                        ki = i
                        kj = j
            for i in kpiece:
                if attacker_pos[0] == i[0]:
                    kpiece.remove(i)
                if attacker_pos[1] == i[1]:
                    kpiece.remove(i)

            if ai == ki:
                s = min(aj, kj)
                b = max(aj, kj)
                for i in range(s, b):
                    beam.append((i, ai))
            elif aj == kj:
                s = min(ai, ki)
                b = max(ai, ki)
                for i in range(s, b):
                    beam.append((aj, i))

            for i in range(len(pos)):
                if pos[i][0][0] == side:
                    sub = []
                    for j in range(len(pos[i])):
                        if j == 0:
                            sub.append(pos[i][j])
                        else:
                            if pos[i][j] in beam:
                                sub.append(pos[i][j])
                    pos[i] = sub


        elif attacker[0] == os and attacker[1] == 'b':
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j][0] == os and table[i][j][1] == 'b':
                        aj = j
                        ai = i
                    elif table[i][j][0] == side and table[i][j][1] == 'k':
                        kj = j
                        ki = i

            beam.append((aj, ai))
            r = abs(kj - aj)

            # Left Bottom (king_pos)
            if kj < aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj + i, ki - i))
                if kj != 0 and ki != 7:
                    kpiece.remove((kj - 1, ki + 1))

            # Left Top
            elif kj < aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj + i, ki + i))
                if kj != 0 and ki != 0:
                    kpiece.remove((kj - 1, ki - 1))

            # Right Bottom
            elif kj > aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj - i, ki - i))
            if kj != 7 and ki != 7:
                kpiece.remove((kj + 1, ki + 1))

            # Right Top
            elif kj > aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj - i, ki + i))
                if kj != 7 and ki != 0:
                    kpiece.remove((kj + 1, ki - 1))

            for i in range(len(pos)):
                if pos[i][0][0] == side:
                    sub = []
                    for j in range(len(pos[i])):
                        if j == 0:
                            sub.append(pos[i][j])
                        else:
                            if pos[i][j] in beam:
                                sub.append(pos[i][j])
                    pos[i] = sub

        elif attacker[0] == os and attacker[1] == 'q':

            # Rook Moves for Queen
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j][0] == os and table[i][j][1] == 'q':
                        attacker_pos = [j, i]
                        aj = j
                        ai = i
                    elif table[i][j][0] == side and table[i][j][1] == 'k':
                        ki = i
                        kj = j
            for i in kpiece:
                if attacker_pos[0] == i[0]:
                    kpiece.remove(i)
                if attacker_pos[1] == i[1]:
                    kpiece.remove(i)

            if ai == ki:
                s = min(aj, kj)
                b = max(aj, kj)
                for i in range(s, b):
                    beam.append((i, ai))
            elif aj == kj:
                s = min(ai, ki)
                b = max(ai, ki)
                for i in range(s, b):
                    beam.append((aj, i))

            # Bishop moves for Queen
            for i in range(len(pos)):
                if pos[i][0][0] == side:
                    sub = []
                    for j in range(len(pos[i])):
                        if j == 0:
                            sub.append(pos[i][j])
                        else:
                            if pos[i][j] in beam:
                                sub.append(pos[i][j])
                    pos[i] = sub

            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j][0] == os and table[i][j][1] == 'q':
                        aj = j
                        ai = i
                    elif table[i][j][0] == side and table[i][j][1] == 'k':
                        kj = j
                        ki = i

            r = abs(kj - aj)

            # Left Bottom (king_pos)
            if kj < aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj + i, ki - i))
                if kj != 0 and ki != 7:
                    kpiece.remove((kj - 1, ki + 1))

            # Left Top
            elif kj < aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj + i, ki + i))
                if kj != 0 and ki != 0:
                    kpiece.remove((kj - 1, ki - 1))

            # Right Bottom
            elif kj > aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj - i, ki - i))
            if kj != 7 and ki != 7:
                kpiece.remove((kj + 1, ki + 1))

            # Right Top
            elif kj > aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj - i, ki + i))
                if kj != 7 and ki != 0:
                    kpiece.remove((kj + 1, ki - 1))

            for i in range(len(pos)):
                if pos[i][0][0] == side:
                    sub = []
                    for j in range(len(pos[i])):
                        if j == 0:
                            sub.append(pos[i][j])
                        else:
                            if pos[i][j] in beam:
                                sub.append(pos[i][j])
                    pos[i] = sub

            if aj != kj and ai != ki:
                beam.append((aj, ai))

        elif attacker[0] == os and attacker[1] in oneshot:
            for i in range(len(table)):
                for j in range(len(table[i])):
                    if table[i][j] == attacker:
                        beam.append((j, i))

    if mode[0] == 'w':
        filtering('b')

    elif mode[1] == 'b':
        filtering('w')


def check_checker(s):
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j][0] == 'w' and table[i][j][1] == 'k' and s == 'white':
                for position in pos:
                    if (j, i) in position:
                        validpos_filter('wcheck', position[0])
                        return 'wcheck'
            if table[i][j][0] == 'b' and table[i][j][1] == 'k' and s == 'black':
                for position in pos:
                    if (j, i) in position:
                        validpos_filter('bcheck', position[0])
                        return 'bcheck'


valid_pos(chance)
check_checker(chance)