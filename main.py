table = [['brl', 'bhl', 'bbl', 'bq', 'bk', 'bbr', 'bhr', 'brr'],
         ['bp0', 'bp1', 'bp2', 'bp3', 'bp4', 'bp5', 'bp6', 'bp7'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['0', '0', '0', '0', '0', '0', '0', '0'],
         ['wp0', 'wp1', 'wp2', 'wp3', 'wp4', 'wp5', 'wp6', 'wp7'],
         ['wrl', 'whl', 'wbl', 'wq', 'wk', 'wbr', 'whr', 'wrr']]
one = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
pure = [1, 1, 1, 1, 1, 1]
c = 1

pos = [['brl'], ['bhl'], ['bbl'], ['bq'], ['bk'], ['bbr'], ['bhr'], ['brr'],
       ['bp0'], ['bp1'], ['bp2'], ['bp3'], ['bp4'], ['bp5'], ['bp6'], ['bp7'],
       ['wp0'], ['wp1'], ['wp2'], ['wp3'], ['wp4'], ['wp5'], ['wp6'], ['wp7'],
       ['wrl'], ['whl'], ['wbl'], ['wq'], ['wk'], ['wbr'], ['whr'], ['wrr']]


def promotion_grid(function=None, oldp=None, newp=None):
    global pos
    if oldp != None and newp != None:
        for i in pos:
            if i[0] == oldp:
                i[0] = newp
    temp_pos = []

    if function == 'reset':
        for i in pos:
            if len(i) == 1:
                temp_pos.append(i)
            elif len(i) != 1:
                while len(i) != 1:
                    i.pop()
                temp_pos.append(i)
        return temp_pos


def promotion(cord_x, cord_y, p):
    old_piece = table[cord_y][cord_x]
    pawn_no = old_piece[2]

    if table[cord_y][cord_x][0] == 'w':
        if p == 'q':
            table[cord_y][cord_x] = f'wq{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'wq{pawn_no}')

        elif p == 'b':
            table[cord_y][cord_x] = f'wbr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'wbr{pawn_no}')

        elif p == 'h':
            table[cord_y][cord_x] = f'whr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'whr{pawn_no}')

        elif p == 'r':
            table[cord_y][cord_x] = f'wrr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'wrr{pawn_no}')

    elif table[cord_y][cord_x][0] == 'b':
        if p == 'q':
            table[cord_y][cord_x] = f'bq{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'bq{pawn_no}')

        elif p == 'b':
            table[cord_y][cord_x] = f'bbr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'bbr{pawn_no}')

        elif p == 'k':
            table[cord_y][cord_x] = f'bhr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'bhr{pawn_no}')

        elif p == 'r':
            table[cord_y][cord_x] = f'brr{table[cord_y][cord_x][2]}'
            promotion_grid(function='change', oldp=old_piece, newp=f'brr{pawn_no}')


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
    pos = promotion_grid('reset')

    for i in range(len(table)):
        for j in range(len(table[i])):

            if table[i][j][0] == 'w':
                if table[i][j][1] == 'p':

                    for piece in pos:
                        if piece[0] == table[i][j]:

                            if i == 6:
                                if table[i - 1][j] == '0':
                                    piece.append((j, i - 1))
                                if table[i - 2][j] == '0' and table[i - 1][j] == '0':
                                    piece.append((j, i - 2))

                            elif i != 6 and i != 0:
                                if table[i - 1][j] == '0':
                                    piece.append((j, i - 1))

                            if j != 0 and i != 0:
                                if table[i - 1][j - 1][0] == 'b':
                                    piece.append((j - 1, i - 1))
                            if j != 7 and i != 0:
                                if table[i - 1][j + 1][0] == 'b':
                                    piece.append((j + 1, i - 1))

                if table[i][j][1] == 'r':
                    if table[i][j][2] == 'r':
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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

                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                    for k in range(len(pos)):
                        if pos[k][0] == table[i][j]:
                            piece = pos[k]

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

                    for k in range(len(pos)):
                        if pos[k][0] == table[i][j]:
                            piece = pos[k]

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

    for i in range(len(table)):
        for j in range(len(table[i])):

            if table[i][j][0] == 'b':
                if table[i][j][1] == 'p':

                    for piece in pos:
                        if piece[0] == table[i][j]:

                            if i == 1:
                                if table[i + 1][j] == '0':
                                    piece.append((j, i + 1))
                                if table[i + 2][j] == '0' and table[i + 1][j] == '0':
                                    piece.append((j, i + 2))

                            elif i != 1 and i != 7:
                                if table[i + 1][j] == '0':
                                    piece.append((j, i + 1))

                            if j != 7 and i != 7:
                                if table[i + 1][j + 1][0] == 'w':
                                    piece.append((j + 1, i + 1))
                            if j != 0 and i != 7:
                                if table[i + 1][j - 1][0] == 'w':
                                    piece.append((j - 1, i + 1))

                if table[i][j][1] == 'r':
                    if table[i][j][2] == 'r':
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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

                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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
                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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

                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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

                        for k in range(len(pos)):
                            if pos[k][0] == table[i][j]:
                                piece = pos[k]

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

                    for k in range(len(pos)):
                        if pos[k][0] == table[i][j]:
                            piece = pos[k]

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
                    for k in range(len(pos)):
                        if pos[k][0] == table[i][j]:
                            piece = pos[k]

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

    return check_checker(chance, pos)


def validpos_filter(status, attacker):
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

            if kj < aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj + i, ki - i))
                if kj != 0 and ki != 7:
                    kpiece.remove((kj - 1, ki + 1))


            elif kj < aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj + i, ki + i))
                if kj != 0 and ki != 0:
                    kpiece.remove((kj - 1, ki - 1))


            elif kj > aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj - i, ki - i))
            if kj != 7 and ki != 7:
                kpiece.remove((kj + 1, ki + 1))


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


            if kj < aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj + i, ki - i))
                if kj != 0 and ki != 7:
                    kpiece.remove((kj - 1, ki + 1))


            elif kj < aj and ki < ai:
                for i in range(1, r):
                    beam.append((kj + i, ki + i))
                if kj != 0 and ki != 0:
                    kpiece.remove((kj - 1, ki - 1))


            elif kj > aj and ki > ai:
                for i in range(1, r):
                    beam.append((kj - i, ki - i))
            if kj != 7 and ki != 7:
                kpiece.remove((kj + 1, ki + 1))


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


    def one_attacker(status, attacker):
        possible_pos = []
        s = 'w' if attacker[0] == 'b' else 'b'

        for i in pos:
            if i[0] == attacker:
                for j in pos:
                    if j[0] == f'{s}k':
                        for a in j:
                            if a in i:
                                j.remove(a)

        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == attacker:
                    attacker_pos = (j, i)
                    possible_pos.append(attacker_pos)


        if attacker[1] == 'r':
            if attacker_pos[0] == king_pos[0]:
                b_min = min((attacker_pos[1], king_pos[1]))
                b_max = max((attacker_pos[1], king_pos[1]))
                step = b_max - b_min - 1

                for i in range(1, step+1):
                    possible_pos.append((attacker_pos[0], b_min+i))


            elif attacker_pos[1] == king_pos[1]:
                b_min = min((attacker_pos[0], king_pos[0]))
                b_max = max((attacker_pos[0], king_pos[0]))
                step = b_max - b_min - 1

                for i in range(1, step+1):
                    possible_pos.append((b_min+i, attacker_pos[1]))

        elif attacker[1] == 'b':
            ai = attacker_pos[1]
            aj = attacker_pos[0]

            ki = king_pos[1]
            kj = king_pos[0]

            bi = max(ai,ki)
            si = min(ai,ki)
            step = bi-si-1


            if ai < ki and aj > kj:
                for i in range(1, step+1):
                    possible_pos.append((attacker_pos[0]-i, attacker_pos[1]+i))

            elif ai < ki and aj < kj:
                for i in range(1, step+1):
                    possible_pos.append((attacker_pos[0]-i, attacker_pos[1]-i))

            elif ai > ki and aj < kj:
                for i in range(1, step+1):
                    possible_pos.append((attacker_pos[0]+i, attacker_pos[1]-i))

            elif ai > ki and aj > kj:
                for i in range(1, step+1):
                    possible_pos.append((attacker_pos[0]+i, attacker_pos[1]+i))


        elif attacker[1] == 'q':
            pass


        # Only possible_pos in pos
        for i in range(len(pos)):
            if pos[i][0][0] == s:
                temp = []
                temp.append(pos[i][0])
                for j in range(len(pos[i])):
                    if j != 0 and pos[i][j] in possible_pos:
                        temp.append(pos[i][j])
                pos[i] = temp

        return pos


    def multi_attacker(status, attacker):
        pass

    if len(attacker) == 1:
        attacker1 = attacker[0]
        return one_attacker(status, attacker1)

    elif len(attacker) > 1:
        return multi_attacker(status, attacker)


log = open('log.txt', 'w')


def check_checker(s, pos):
    if s == 'white':
        king = 'wk'
        status = 'wcheck'

    elif s == 'black':
        king = 'bk'
        status = 'bcheck'

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == king:
                global king_pos
                king_pos = (j, i)

    attackers = []
    for i in pos:
        if king_pos in i:
            attackers.append(i[0])

    if len(attackers) == 0:
        return pos

    elif len(attackers) == 1:
        log.write('check 1dude')
        return validpos_filter(status, attackers)

    elif len(attackers) > 1:
        return validpos_filter(status, attackers)

a = valid_pos('white')
for i in a:
    if len(i) != 1:
        print(i)