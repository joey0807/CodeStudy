n = int(input())
line = list(map(int, input().split()))
ans = [0]*n

for x in range(n):
    index = 0 #시작값 0
    for y in range(n):
        if index == line[x] and ans[y] == 0:
            ans[y] = x + 1 
            break
        elif ans[y] == 0: 
            index += 1

print(*ans)