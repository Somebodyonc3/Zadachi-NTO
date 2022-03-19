def encode(bits):
    plaintext = []
    n = len(bits)
    q = n // 8
    r = n % 8

    for i in range(q):
        # срез: очередные 8 битов входного списка
        x0, x1, x2, x3, x4, x5, x6, x7 = bits[8 * i : 8 * (i + 1)]
        plaintext.append((x0, x1, x2, x3))
        plaintext.append((x4, x5, x6, x7))

    # добавляем в конец списка битов нули, чтобы длина "хвоста" стала равна 8
    if r != 0:
        x0, x1, x2, x3, x4, x5, x6, x7 = bits[8 * q : ] + (8 - r) * [0]
        plaintext.append((x0, x1, x2, x3))
        plaintext.append((x4, x5, x6, x7))

    # Порождающая матрица
    G = [
            [0, 1, 1, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 1, 0, 0],
            [1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 1, 0, 0, 0, 0, 1]
        ]

    encoded = []
    #Само кодирование, вектор умножаем на матрицу
    for u in plaintext:
        c = 8 * [0]
        c_byte = 0
        for i in range(8):
            for j in range(4):
                c[i] += u[j] * G[j][i]
            c[i] %= 2
        encoded.extend(c) # обрати внимание: не append, а extend

    return encoded


def decode(bits):
    H = [
            [1, 0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 1, 1, 1, 0]
        ]
    # в какой позиции кода ошибка
    locator = [
            [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1],
            [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]
        ]

    decoded = []

    n = len(bits)
    q = n // 8 # будем считать, что количество битов делится нацело на 8,
               # потому что при кодировании получается именно такое количество

    # исправление ошибки
    for i in range(q):
        # срез: очередные 8 битов входного списка
        c_bits = bits[8 * i : 8 * (i + 1)]
        syndrome = 4 * [0]
        for i in range(4):
            for j in range(8):
                syndrome[i] += H[i][j] * c_bits[j]
            syndrome[i] %= 2
        try:
            k = locator.index(syndrome)
            c_bits[k] = (c_bits[k] + 1) % 2
        except:
            pass

        decoded.extend(c_bits[4:])

    return decoded

'''
#ПРИМЕР
x = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]
print('Исходное сообщение:', x)
print()

y = encode(x)
print('Закодированная последовательность:', y)
print()

y1 = y.copy()
y1[0] = (y1[0] + 1) % 2 # вектор ошибок
print('Закодированное сообщение с ошибкой:', y1, y == y1)
print()

z = decode(y)
print('Раскодированная последовательность:', z, x == z)
'''