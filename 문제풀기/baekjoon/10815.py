from collections import Counter

n = int(input())
nList = list(map(int, input().split()))
m = int(input())
mList = list(map(int, input().split()))

ans = [0]*m

count = Counter(nList)

for x in range(m):
    if mList[x] in count:
        print(1,end=' ')
    else:
        print(0,end=' ')