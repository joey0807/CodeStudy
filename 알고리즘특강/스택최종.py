##함수
def isStackFull(): #스택이 꽉 찼는지 확인하는 함수
  global SIZE, stack, top
  if (top >= SIZE-1):
    return True
  else:
    return False

def push(data): #데이터 삽입 함수
  global SIZE, stack, top
  if(isStackFull()):
    print('stack이 꽉 찼다')
    return
  top += 1
  stack[top] = data

def isStackEmpty(): #스택이 비었는지 확인하는 함수
  global SIZE, stack, top
  if(top<=-1):
    return True
  else:
    return False

def pop(): #스택에서 데이터를 추출하는 함수
  global SIZE, stack, top
  if(isStackEmpty()):
    print('stack이 비었다')
    return None
  data = stack[top]
  stack[top] = None
  top -= 1
  return data

def peek(): #스택에서 top 위치의 데이터를 확인하는 함수
  global SIZE, stack, top
  if(isStackEmpty()):
    print('stack이 비었다')
    return None
  return stack[top]

##전역
SIZE = int(input('스택 크기를 입력하세요 : '))
stack = [None for _ in range(SIZE)]
top = -1

##메인
if __name__ == '__main__':
  select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')

  while(select != 'X' and select != 'x'):
    if select == 'I' or select == 'i':
      data = input('입력할 데이터 : ')
      push(data)
      print('스택 상태 : ', stack)

    elif select =='E' or select == 'e':
      data = pop()
      print('추출된 데이터 : ', data)
      print('스택 상태 : ', stack)

    elif select == 'V' or select == 'v':
      data = peek()
      print('확인된 데이터 : ', data)
      print('스택 상태 : ', stack)

    else:
      print('입력이 잘못됨')

    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')

  print('종료')