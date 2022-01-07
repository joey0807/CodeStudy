#스택 데이터 삽입과 삭제
##함수

##전역
SIZE = 5
stack = [None for _ in range(SIZE)] #전역변수 크기만큼의 빈 배열 생성
top = -1 #스택은 top 값이 -1부터 시작

##메인
#데이터 삽입 : push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
print(stack) #삽입할 때는 top을 1씩 증가시키고 데이터를 넣음

#데이터 삭제 : pop
data = stack[top]
stack[top] = None
top -= 1
print('팝 => ',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝 => ',data)

data = stack[top]
stack[top] = None
top -= 1
print('팝 => ',data)
print(stack) #데이터를 삭제한 후 top을 1씩 감소시킴