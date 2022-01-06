#단순 연결 리스트 생성 함수 
##함수
class Node() :
    def __init__(self):
        self.data = None
        self.link = None
def printNodes(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

##전역
memory=[]
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

##메인
node = Node()  # 첫 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:] :  # ['정연', '쯔위', '사나', '지효']
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)