n = int(input())
atm = list(map(int, input().split()))
ans = 0
atm.sort()

for x in range(n):
    for y in range(x+1):
        ans += atm[y]

print(ans)    