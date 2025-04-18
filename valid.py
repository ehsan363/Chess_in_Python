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
                    print('piece = ',table[i][j])
                    if table[i][j][1] == 'p':
                        print('Entered pawn')
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
                        print('entered rook')
                        if table[i][j][2] == 'r':
                            piece = pos[31]
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
                                        for r in range(j + 1,8):
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
                                        for l in range(j-1,-1,-1):
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
                                        for r in range(j+1,8):
                                            if table[i][r][0] == 'w':
                                                break
                                            if table[i][r][0] == '0':
                                                piece.append((r, i))
                                            elif table[i][r][0] == 'b':
                                                piece.append((r, i))
                                                break
                                elif move == 3:
                                    if i != 7:
                                        for d in range(i +1, 8):
                                            if table[d][j][0] == 'w':
                                                break
                                            if table[d][j][0] == '0':
                                                piece.append((j, d))
                                            elif table[d][j][0] == 'b':
                                                piece.append((j, d))
                                                break


                    if table[i][j][1] == 'h':
                        print('entered knight')
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
                        print('entered bishop')
                        if table[i][j][2] == 'l':
                            piece = pos[26]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move,i,j)
                                        for ur in range(1,dis+1):
                                            if table[i-ur][j+ur][0] == 'w':
                                                break
                                            if table[i-ur][j+ur][0] == '0':
                                                piece.append((j+ur, i-ur))
                                            elif table[i-ur][j+ur][0] == 'b':
                                                piece.append((j+ur, i-ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move,i,j)
                                        for dr in range(1,dis+1):
                                            if table[i+dr][j+dr][0] == 'w':
                                                break
                                            elif table[i+dr][j+dr][0] == '0':
                                                piece.append((j+dr,i+dr))
                                            elif table[i + dr][j + dr][0] == 'b':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move,i, j)
                                        for dl in range(1,dis+1):
                                            if table[i+dl][j-dl][0] == 'w':
                                                break
                                            elif table[i+dl][j-dl][0] == '0':
                                                piece.append((j-dl, i+dl))
                                            elif table[i + dl][j-dl][0] == 'b':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move,i, j)
                                        for ul in range(1,dis+1):
                                            if table[i-ul][j-ul][0] == 'w':
                                                break
                                            elif table[i-ul][j-ul][0] == '0':
                                                piece.append((j-ul, i-ul))
                                            elif table[i-ul][j-ul][0] == 'b':
                                                piece.append((j-ul, i-ul))
                                                break


                        elif table[i][j][2] == 'r':
                            piece = pos[29]
                            for move in range(4):

                                if move == 0:
                                    if j != 7 and i != 0:
                                        distance(move,i,j)
                                        for ur in range(1,dis+1):
                                            if table[i-ur][j+ur][0] == 'w':
                                                break
                                            if table[i-ur][j+ur][0] == '0':
                                                piece.append((j+ur, i-ur))
                                            elif table[i-ur][j+ur][0] == 'b':
                                                piece.append((j+ur, i-ur))
                                                break


                                elif move == 1:
                                    if j != 7 and i != 7:
                                        distance(move,i,j)
                                        for dr in range(1,dis+1):
                                            if table[i+dr][j+dr][0] == 'w':
                                                break
                                            elif table[i+dr][j+dr][0] == '0':
                                                piece.append((j+dr,i+dr))
                                            elif table[i + dr][j + dr][0] == 'b':
                                                piece.append((j + dr, i + dr))
                                                break

                                elif move == 2:
                                    if j != 0 and i != 7:
                                        distance(move,i, j)
                                        for dl in range(1,dis+1):
                                            if table[i+dl][j-dl][0] == 'w':
                                                break
                                            elif table[i+dl][j-dl][0] == '0':
                                                piece.append((j-dl, i+dl))
                                            elif table[i + dl][j-dl][0] == 'b':
                                                piece.append((j - dl, i + dl))
                                                break

                                elif move == 3:
                                    if j != 0 and i != 0:
                                        distance(move,i, j)
                                        for ul in range(1,dis+1):
                                            if table[i-ul][j-ul][0] == 'w':
                                                break
                                            elif table[i-ul][j-ul][0] == '0':
                                                piece.append((j-ul, i-ul))
                                            elif table[i-ul][j-ul][0] == 'b':
                                                piece.append((j-ul, i-ul))
                                                break
                    if table[i][j][1] == 'k':
                        print('entered king')
                        piece = pos[28]
                        if  i != 0:
                            if table[i-1][j][0] != 'w':
                                print('#1')
                                piece.append((j, i-1))
                        if i != 0 and j != 0:
                            if table[i-1][j-1][0] != 'w':
                                print('#2')
                                piece.append((j-1, i-1))
                        if j != 0:
                            if table[i][j-1][0] != 'w':
                                print('#3')
                                piece.append((j-1, i))
                        if j != 0 and i != 7:
                            if table[i+1][j-1][0] != 'w':
                                print('#4')
                                piece.append((j-1, i+1))
                        if i != 7:
                            if table[i+1][j][0] != 'w':
                                print('#5')
                                piece.append((j, i+1))
                        if i != 7 and j != 7:
                            if table[i+1][j+1][0] != 'w':
                                print('#6')
                                piece.append((j+1, i+1))
                        if j != 7:
                            if table[i][j+1][0] != 'w':
                                print('#7')
                                piece.append((j+1, i))


                    if table[i][j][1] == 'q':
                        print('entered queen')
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
                            #####################################33333
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






    elif chance == 'black':
        print()

    print(pos)
    print('####################################')
    cm = 0
    for i in pos:
        if len(i) != 1:
            cm += (len(i) - 1)
            print(i)
    print(cm)


valid_pos(chance)