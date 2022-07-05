from collections import deque

queue = deque()
y = []

n, k = map(int, input().split())

for x in range(1,n+1):
    queue.append(x)
    #print(queue)

#deque에서 첫 번째 원소를 제거할 때 : popleft()
while queue:
    for i in range(k-1):
        queue.append(queue.popleft()) #첫 번째 원소를 queue 마지막에 추가하고 첫 번째 원소는 제거 -> 첫 번째 값을 맨 뒤로 이동
        #print(queue)
    y.append(queue.popleft()) #k번째 원소를 y리스트에 추가
    #print(y)

print('<',end='')
for x in range(len(y)-1):
    print(y[x],end=', ')
print(y[-1],end='>')