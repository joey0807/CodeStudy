#플로이드 워셜 알고리즘 점화식 : D(ab) = min(D(ab), D(ak) + D(kb))

INF = int(1e9)

n = int(input()) #노드 개수 n
m = int(input()) #간선 개수 m

#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신에게 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

#수행 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print('Infinity', end=' ') #도달할 수 없는 경우 Infinity 출력
        else:
            print(graph[a][b], end=' ')
    print()