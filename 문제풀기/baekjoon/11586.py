n = int(input())
mirror = []
for i in range(n):
    a = input()
    mirror.append(a)
k = int(input())

if k == 1:
    for x in range(n):
        print(mirror[x])

if k == 2:
    for x in range(n):
        print(mirror[x][::-1])

if k == 3:
    for x in range(n-1,-1,-1):
        print(mirror[x])