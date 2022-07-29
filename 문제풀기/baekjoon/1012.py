import sys
sys.setrecursionlimit(10**6) #문제 풀이를 위해 재귀 깊이를 더 깊게 설정

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] += 1

    # for x in range(n):
    #     for y in range(m):
    #         print(graph[x][y],end=' ')
    #     print()

    def dfs(x, y):
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False
        
        if graph[x][y] == 1:
            graph[x][y] = 0

            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x,y+1)
            
            return True
        return False

    count = 0
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                count += 1

    print(count)