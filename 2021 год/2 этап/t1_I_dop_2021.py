s1 = 'horse'
s2 = 'ubjsd'
p = [#1234 => 0123
    #abcdefghijklmnopqrstuvwxyz
    'qwertyuiopasdfghjklzxcvbnm',
    'qwertyuiopasdfghjklzxcvbnm',
    'qwertyuiopasdfghjklzxcvbnm',
    'qwertyuiopasdfghjklzxcvbnm']

import itertools
allp = list(itertools.product('0123', repeat=4))

ans = set()

for x in allp[:4]:
    t1 = p[int(x[0])]
    t2 = p[int(x[1])]
    t3 = p[int(x[2])]
    t4 = p[int(x[3])]
    letter1 = s1[0]
    t1let = ord(letter1) - ord('a')
    letter2 = t1[t1let]
    t1let = ord(letter2) - ord('a')
    letter3 = t2[t1let]
    t1let = ord(letter3) - ord('a')
    letter4 = t3[t1let]
    t1let = ord(letter4) - ord('a')
    letter5 = t4[t1let]
    if letter1 == letter5:
        ans.add((t1, t2, t3, t4))
    else:
        ans -= (t1, t2, t3, t4)
        continue
    print(letter1, letter2, letter3, letter4, letter5)

