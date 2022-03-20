
def encode(bits):                                                        # Кодировка сообщения
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
                                                                            # Само кодирование, вектор умножаем на матрицу
    for u in plaintext:
        c = 8 * [0]
        c_byte = 0
        for i in range(8):
            for j in range(4):
                c[i] += u[j] * G[j][i]
            c[i] %= 2
        encoded.extend(c)                                                   # обрати внимание: не append, а extend

    return encoded



x = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1]
print('Исходное сообщение:', x)

y = encode(x)
print('Закодированная последовательность:', y)


