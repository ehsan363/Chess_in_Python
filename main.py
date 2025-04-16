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
