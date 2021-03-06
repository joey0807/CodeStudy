##함수
class TreeNode():
  def __init__(self):
    self.left = None
    self.data = None
    self.right = None

##전역
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

##메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]: #['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']
  node  = TreeNode()
  node.data = name

  current = root
  while True: #None 나올때까지(자리 잡을 때 까지) 반복
    if name < current.data:
      if current.left == None:
        current.left = node
        break 
      current = current.left
    else:
      if current.right == None:
        current.right = node
        break 
      current = current.right

  memory.append(node)

print('이진 탐색 트리 구성 완료')

###이진 탐색 트리의 활용(검색)
###검색의 순서 : 성공(값)이나 실패(None)할 때 까지
findName = '마마무'
current = root
while True:
  if findName == current.data:
    print(findName, '찾기 완료!')
    break
  elif findName <= current.data:
    if current.left == None:
      print(findName, '없음 ㅠ')
      break
    current = current.left
  else:
    if current.right == None:
      print(findName, '없음 ㅠ')
      break
    current = current.right

print('종료')