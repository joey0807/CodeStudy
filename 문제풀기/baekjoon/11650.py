n = int(input())
s = []
for i in range(n):
    x, y = map(int, input().split())
    s.append((x,y))

s.sort()

for x in range(n):
    print(*s[x])