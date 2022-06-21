n, m = map(int, input().split())

bbang = []
for x in range(n):
    bread = input()
    bbang.append(bread)

for x in range(n):
    fall = bbang[x][::-1]
    print(fall)
