import sys, heapq

n = int(sys.stdin.readline().rstrip())
h = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if h:
            print(h[0][1])
            heapq.heappop(h)
        else:
            print(0)
    else:
        heapq.heappush(h,(abs(x),x))
