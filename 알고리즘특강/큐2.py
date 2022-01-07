##함수
def isQueueFull(): #큐가 꽉 찼는지 확인하는 함수
  global SIZE, queue, front, rear
  if(rear != SIZE-1):
    return False
  elif(rear == SIZE-1) and (front == -1):
    return True
  else:
    for i in range(front+1, SIZE):
      queue[i-1] = queue[i]
      queue[i] = None
    front -= 1
    rear -= 1
    return False

def enQueue(data): #큐에 데이터를 삽입하는 함수
  global SIZE, queue, front, rear
  if (isQueueFull()):
    print('큐 꽉참')
    return
  rear += 1
  queue[rear] = data

def isQueueEmpty(): #큐가 비었는지 확인하는 함수
  global SIZE, queue, front, rear
  if(front == rear):
    print('큐 비었음')
    return True
  else:
    return False

def deQueue(): #큐에서 데이터를 추출하는 함수
  global SIZE, queue, front, rear
  if(isQueueEmpty()):
    print('큐 비었음')
    return None
  front += 1
  data = queue[front]
  queue[front] = None
  return data

def peek(): #큐에서 front+1 위치의 데이터를 확인하는 함수
  global SIZE, queue, front, rear
  if(isQueueEmpty()):
    print('큐 비었음')
    return None
  
  return queue[front+1]

##전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

##메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')
print('입장 손님 : ', deQueue())
print('입장 손님 : ', deQueue())
print('출구<--', queue, '<--입구')
enQueue('힊붕이')
print('출구<--', queue, '<--입구')
enQueue('솔붕이')
print('출구<--', queue, '<--입구')
enQueue('훈붕이')
print('출구<--', queue, '<--입구')