#단순 연결 리스트 생성
##함수
#노드 생성 : 클래스라는 문법을 사용해서 Node 데이터형을 정의
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

# print(node1.data, end=' ')
# print(node1.link.data, end=' ')
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')

current = node1 #첫 번째 노드를 현재(current) 노드로 지정
print(current.data, end=' ')
while current.link != None: #현재 노드의 링크가 비어있지 않다면 반복, 반복하다 현재 노드의 링크가 비어 있으면 종료
    current = current.link #현재 노드를 링크가 가르키는 노드로 변경
    print(current.data, end=' ') #변경한 후 현재의 노드 데이터 출력