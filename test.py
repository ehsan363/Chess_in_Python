'''s=1
                            while s == 1:
                                if m == 0:
                                    print('entered m0')
                                    if j != 0:
                                        print('entered')
                                        if table[i][j-1] == '0':
                                            pos.append((i,j-1))
                                        elif table[i][j-1] != '0' and table[i][j-1][0] =='b':
                                            pos.append((i,j-1))
                                            s -= 1
                                        else:
                                            break
                                    else:
                                        s -= 1

                                elif m == 1:
                                    print('entered m1')
                                    if i != 0:
                                        print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
                                        print('i-1',table[i-1])
                                        print('[i-1] [j]',table[i-1][j])
                                        if table[i -1][j] == '0':
                                            print('1')
                                            pos.append((i-1,j))
                                        elif table[i - 1][j] != '0' and table[i-1][j][0] == 'b':
                                            print('2')
                                            pos.append((i-1,j))
                                            s -= 1
                                        else:
                                            print('3')
                                            break
                                    else:
                                        s -= 1

                                elif m == 2:
                                    if j != 7:
                                        if table[i][j+1] == '0':
                                            pos.append((i,j+1))
                                        elif table[i][j+1] != '0' and table[i][j+1] == 'b':
                                            pos.append((i,j+1))
                                            s-=1
                                        else:
                                            break
                                    else:
                                        s -= 1

                                elif m == 3:
                                    if i != 7:
                                        if table[i+1][j] == '0':
                                            pos.append(([i+1][j]))
                                        elif table[i+1][j] != '0' and table[i+1][j] == 'b':
                                            pos.append(([i+1][j]))
                                            s-=1
                                        else:
                                            break
                                    else:
                                        s -= 1
'''

s = []
for i in range(32):
    s.append([])

print(s)