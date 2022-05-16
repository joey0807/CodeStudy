n, m = map(int, input().split())
castle = []
a = 0
b = 0

for i in range(n):
    castle.append(input())

for x in range(n):
    if 'X' not in castle[x]:
        a += 1

for y in range(m):
    if 'X' not in [castle[x][y] for x in range(n)]:
        b += 1

print(max(a,b))