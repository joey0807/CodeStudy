import sys, heapq #빠른 계산을 위한 sys, heapq 함수

#heapq : O(NlogN)에 오름차순 정렬이 완료됨
n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if arr:
            print(arr[0])
            heapq.heappop(arr)
        else:
            print(0)
        
    else:
        heapq.heappush(arr,x)