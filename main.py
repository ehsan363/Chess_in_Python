def table_creation():
    table = []
    for i in range(8):
        table.append([0,0,0,0,0,0,0,0])

    table[0][0] = 'br'
    table[0][1] = 'bh'
    table[0][2] = 'bbr'
    table[0][3] = 'bq'
    table[0][4] = 'bk'
    table[0][5] = 'bbl'
    table[0][6] = 'bh'
    table[0][7] = 'br'

    table[7][0] = 'wr'
    table[7][1] = 'wh'
    table[7][2] = 'wbr'
    table[7][3] = 'wq'
    table[7][4] = 'wk'
    table[7][5] = 'wbl'
    table[7][6] = 'wh'
    table[7][7] = 'wr'

    for i in range(2):
        if i == 0:
            pc = 'w'
            pcn = 6
        if i == 1:
            pc = 'b'
            pcn = 1
        if i == 2: break

        for j in range(8):
            table[pcn][j] = pc+'p'+str(j)

    for i in table:
        print(i)

def move_available(m):
    a

def player_turn():
    a = 2
    while a!=0  or a!=1:

        print(a/2 == int(a/2))
        print(a/2 != int(a/2))

        if a/2 == int(a/2):
            print('white',a)
            turn = 'white'
        elif a/2 != int(a/2):
            print('black',a)
            turn = 'black'
        a+=1
        if turn == 'white':
            print('white turn')

        elif turn == 'black':
            print('black turn')


    if a==0:
        print('White Won!!!')
    if a==-1:
        print('Black Won!!!')
    else:
        print('Something went WRONG!!!')
        print('currently a =',a)
player_turn()