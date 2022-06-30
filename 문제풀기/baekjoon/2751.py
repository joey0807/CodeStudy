import sys

n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    a = int(sys.stdin.readline())
    ans.append(a)

ans.sort()

for x in ans:
    sys.stdout.write(str(x)+'\n')