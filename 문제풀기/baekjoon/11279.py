import heapq, sys

n = int(sys.stdin.readline().strip())
s = []

#heapq는 최소 힙만 제공 -> 최대 힙을 구현하려면 값의 부호를 임시로 변경하는 방법 사용
for _ in range(n):
    x = int(sys.stdin.readline().strip())

    if x == 0:
        if s:
            print(-s[0])
            heapq.heappop(s)
        else:
            print(0)

    else:
        heapq.heappush(s,-x)