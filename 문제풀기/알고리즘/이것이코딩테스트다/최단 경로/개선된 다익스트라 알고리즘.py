import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드의 개수 n, 간선의 개수 m
start = int(input()) #시작 노드 번호 
graph = [[] for i in range(n+1)] #각 노드에 연결되어있는 노드에 대한 정보를 담는 리스트
distance = [INF] * (n+1) #최단 거리 테이블을 모두 무한으로 초기화

#모든 간선 정보 입력받기
for _ in range(m):
    a,b,c = map(int, input().split()) #a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #시작 노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입
    distance[start] = 0
    while q: #q가 비어있지 않다면
        dist, now = heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        if distance[now] < dist: #현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]: #현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]

            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

#다익스트라 알고리즘 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print('Infinity') #도달할 수 없는 경우, Infinity 출력
    else:
        print(distance[i])