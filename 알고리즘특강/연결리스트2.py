#노드 중간에 데이터 삽입과 삭제
##함수
class Node(): #Node라는 데이터형 만들기
    def __init__(self): #데이터형을 생성할 때 자동으로 실행되는 부분
        self.data = None #데이터 링크가 저장되는 부분
        self.link = None

##전역

##메인
node1 = Node() #첫 번째 노드 생성
node1.data = '다현'

node2 = Node() #두 번째 노드 생성
node2.data = '정연'
node1.link = node2 #첫 번째 노드의 링크에 두 번째 노드를 넣어서 연결

node3 = Node() #세 번째 노드 생성
node3.data = '쯔위'
node2.link = node3 #마찬가지로 두 번째 노드의 링크에 세 번째 노드를 넣어서 연결

node4 = Node() #네 번째 노드 생성
node4.data = '사나'
node3.link = node4 

node5 = Node() #다섯 번째 노드 생성
node5.data = '지효'
node4.link = node5

#삽입
newNode = Node()
newNode.data = '힊붕이' #새로운 데이터
newNode.link = node2.link #새로운 데이터의 링크가 3번째 노드를 가르키게
node2.link = newNode #기존의 두 번째 링크가 새로운 데이터 노드를 가르키게 바꿔주기

current = node1 #첫 번째 노드를 현재(current) 노드로 지정
print(current.data, end=' ')
while current.link != None: #현재 노드의 링크가 비어있지 않다면 반복, 반복하다 현재 노드의 링크가 비어 있으면 종료
    current = current.link #현재 노드를 링크가 가르키는 노드로 변경
    print(current.data, end=' ') #변경한 후 현재의 노드 데이터 출력

#삭제
node2.link = newNode.link #삭제하고 싶은 데이터의 다음 링크를 그 데이터 앞 링크로 복사
del(newNode) #데이터 삭제
print()

current = node1 #첫 번째 노드를 현재(current) 노드로 지정
print(current.data, end=' ')
while current.link != None: #현재 노드의 링크가 비어있지 않다면 반복, 반복하다 현재 노드의 링크가 비어 있으면 종료
    current = current.link #현재 노드를 링크가 가르키는 노드로 변경
    print(current.data, end=' ') #변경한 후 현재의 노드 데이터 출력