n = int(input())
load = list(map(int, input().split()))

load.sort()
ans = 0

for x in range(n-1):
    ans += load[x]

print(ans)