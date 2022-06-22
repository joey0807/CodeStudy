chess = []
for x in range(8):
    s = input()
    chess.append(s)
count = 0

for x in range(8):
    if x%2 == 0:
        for y in range(0,8,2):
            if chess[x][y] == 'F':
                count += 1

    if x%2 == 1:
        for y in range(1,8,2):
            if chess[x][y] == 'F':
                count += 1

print(count)
