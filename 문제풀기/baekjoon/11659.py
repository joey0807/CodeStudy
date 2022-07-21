import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
#prefix sum 알고리즘
prefix = [0]

count = 0
for x in arr:
    count += x
    prefix.append(count) #prefix 리스트에 arr 리스트의 누적합 저장

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    print(prefix[y] - prefix[x-1])