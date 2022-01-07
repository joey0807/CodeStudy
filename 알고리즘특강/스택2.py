#top 위치의 데이터를 확인
##함수
def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

def peek():
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택이 비었음')
        return None
    return stack[top]

##전역
SIZE = 5
stack = ['커피', '녹차', '꿀물', None, None] 
top = 2

##메인
print(stack)
retData = peek()
print('top 데이터 확인 : ', retData)
print(stack)