#원형큐 : 큐의 처음과 끝이 연결된 구조
#큐와 다르게 front와 rear의 기본값이 0임
#front와 rear 값이 동일하면 비어있다는 의미 -> rear+1과 front가 같은 경우에는 원형 큐가 꽉 찬 것으로 처리
# if((rear+1)%SIZE == front): 큐가 꽉 차있음!
##함수
def isQueueFull():
  global SIZE, queue, front, rear
  if((rear+1)%SIZE == front): #원형 큐가 꽉 찬 경우인지 확인
    return True
  else:
    return False

def enQueue(data):
  global SIZE, queue, front, rear
  if (isQueueFull()):
    print('큐 꽉참')
    return
  rear = (rear+1) % SIZE
  queue[rear] = data

def isQueueEmpty():
  global SIZE, queue, front, rear
  if(front == rear):
    print('큐 비었음')
    return True
  else:
    return False

def deQueue():
  global SIZE, queue, front, rear
  if(isQueueEmpty()):
    print('큐 비었음')
    return None
  front = (front+1) % SIZE
  data = queue[front]
  queue[front] = None
  return data

def peek():
  global SIZE, queue, front, rear
  if(isQueueEmpty()):
    print('큐 비었음')
    return None
  
  return queue[(front+1)%SIZE]

##전역
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0

##메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

print('입장 손님 : ',deQueue())
print('입장 손님 : ',deQueue())
print('출구<--', queue, '<--입구')

enQueue('선미')
print('출구<--', queue, '<--입구')