n = int(input())
s = []

for i in range(n):
    x, y = map(int, input().split())
    s.append((x,y))

sort_s = sorted(s, key=lambda x : (x[1],x[0]))

for j in sort_s:
    print(j[0],j[1])