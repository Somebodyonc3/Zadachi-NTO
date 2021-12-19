q = 2

Answer = []

for z in range(q):

    dic = {1:[], 2:[], 3:[]}

    for i in range(7):
        x = input()
        if '3' in x:
            dic[3] = (i, x.find('3'))
        elif '2' in x:
            dic[2].append((i, x.find('2')))
        elif '1' in x:
            dic[1].append((i, x.find('1')))


    if len(dic[3]) > 0:
        Answer.append(f'{dic[3][1] -3},{dic[3][0] -3}')
    elif len(dic[2]) > 0:
        t = dic[2][0]
        if t[0] == 0:
            Answer.append(f'{t[1] - 3},-4')
        elif t[0] == 6:
            Answer.append(f'{t[1] - 3},4')
        elif t[1] == 0:
            Answer.append(f'-4,{t[0] - 3}')
        else:
            Answer.append(f'4,{t[0] - 3}')

    else:
        t = dic[1][0]
        if t[0] == 0:
            Answer.append(f'{t[1] - 3},-5')
        elif t[0] == 6:
            Answer.append(f'{t[1] - 3},5')
        elif t[1] == 0:
            Answer.append(f'-5,{t[0] - 3}')
        else:
            Answer.append(f'5,{t[0] - 3}')
    if z < q - 1:
        input()
print(*Answer, sep = '\n')

#print(dic)
#{1: [(1, 3), (5, 3)], 2: [(2, 3), (4, 3), (3, 2), (3, 4)], 3: (3, 3)}