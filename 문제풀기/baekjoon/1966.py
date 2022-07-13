from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    index = deque(0 for _ in range(n)) #빈 리스트 생성 후
    index[m] = 1 #원하는 문서의 위치 확인을 위해 1 삽입
    count = 0 #인쇄된 횟수 확인

    while True:
        if queue[0] == max(queue): #queue의 첫번째 값이 queue의 최대값이면
            count += 1 #인쇄 횟수 1 추가

            if index[0] != 1: #원하는 문서(1)이 아니라면
                queue.popleft() #queue와 index 첫 번째 값 삭제
                index.popleft()
            else: #원하는 문서라면
                print(count) #인쇄된 횟수 출력 후 종료
                break
        else: #queue의 첫 번째 값이 최대값이 아니면
            queue.append(queue[0]) #queue와 index의 첫 번째 값을 맨 뒤로 보낸 후 삭제
            index.append(index[0])
            queue.popleft()
            index.popleft()    