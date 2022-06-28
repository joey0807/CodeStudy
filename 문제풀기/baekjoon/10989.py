import sys

n = int(sys.stdin.readline())
ans = [0]*10001
for i in range(n):
    x = int(sys.stdin.readline())
    ans[x] += 1

for j in range(10001):
    if ans[j] != 0:
        for k in range(ans[j]):
            print(j)