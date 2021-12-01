#Двое мальчиков обмениваются сообщениями с помощью самолётиков. А чтобы их сообщение не прочитал кто-нибудь ещё, если самолётик улетит не туда, они шифруют текст послания по заранее оговоренному алфавиту замены.

#Ваша задача: написать программу, которая по известному алфавиту будет декодировать одно сообщение и кодировать другое.

#Алфавит имеет следующий вид:

#a - bj7a | b - mba1 | c - 7fva | d - 5fjb
#e - 07na | f - 11jf | g - vfyt | h - vg8k 
#i - zfum | j - evun | k - i7an | l - ao8n
#m - amby | n - bka4 | o - rknm | p - 47an
#q - vlya | r - qdqf | s - ikmj | t - ufnu
#u - 01nn | v - asd4 | w - 777d | x - 9kna
#y - nbru | z - illb |          |
#Входной формат: две строки. Первая строка содержит сообщение, которое необходимо дешифровать. Вторая, сообщение, которое нужно зашифровать.
coding = {'a': 'bj7a', 'b': 'mba1', 'c': '7fva', 'd': '5fjb', 'e': '07na', 'f': '11jf', 'g': 'vfyt', 'h': 'vg8k', 'i': 'zfum', 'j': 'evun', 'k': 'i7an','l': 'ao8n', 'm': 'amby', 'n': 'bka4', 'o': 'rknm', 'p': '47an', 'q': 'vlya', 'r': 'qdqf', 's': 'ikmj', 't': 'ufnu', 'u': '01nn', 'v': 'asd4','w': '777d', 'x': '9kna', 'y': 'nbru', 'z': 'illb'}

encoding = dict()

for letter in coding:
    code = coding[letter]
    encoding[code] = letter

ciphertext = input()
plaintext = input()

result1 = []

for i in range(len(ciphertext) // 4):
    block = ciphertext[4 * i : 4 * i + 4]
    if block in encoding:
        result1.append(encoding[block])
    else:
        result1.append(block)

print("".join(result1))

result2 = []

for letter in plaintext:
    if letter in coding:
        result2.append(coding[letter])

print("".join(result2))
