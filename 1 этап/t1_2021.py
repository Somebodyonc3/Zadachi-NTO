#количество ходов коня
x = int(input())
y = int(input())
c = 0
for x1 in range(1, 9):
    for y1 in range(1, 9):
        dx = abs(x - x1)
        dy = abs(y - y1)
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            c += 1
print(c)