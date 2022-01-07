#큐의 데이터 삽입과 추출
##함수

##전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1 #큐에서는 front와 rear가 같은 값인 -1로 시작

##메인
#enQueue : 데이터 삽입
rear += 1
queue[rear] = '화사' #rear값에 1을 더하고 데이터 입력

rear += 1
queue[rear] = '솔라'

rear += 1
queue[rear] = '문별'

print('출구 <--', queue, '<--입구')

#deQueue : 데이터 추출
front += 1 #front 값에 1을 더한 위치의 데이터 삭제
data = queue[front]
queue[front] = None
print('식사할 손님 : ', data)

front += 1
data = queue[front]
queue[front] = None
print('식사할 손님 : ', data)

front += 1
data = queue[front]
queue[front] = None
print('식사할 손님 : ', data)
print('출구 <--', queue, '<--입구')