#이진트리
T = int(input()) #테스트케이스 개수 T

def makeTree(n): 
  global count
  if n <= N: #입력받은 숫자보다 배열의 크기가 넘어가지 않게
    makeTree(n*2) #왼쪽 노드는 현재 인덱스의 2배
    tree[n] = count #더 왼쪽으로 못가면 값 넣기 - 루트값
    count += 1 #값 넣었으면 증가시키기
    makeTree(n*2+1) #오른쪽 노드는 인덱스 2배+1

for i in range(T): #테스트케이스 T만큼 반복
  N = int(input()) #배열 크기 N 입력
  tree = [0 for _ in range(N+1)] #N 크기만큼의 빈 배열 생성
  count = 1 #1부터 계산 시작
  makeTree(1) #이진트리 1부터 시작 

  print('#{} {} {}'.format(i+1,tree[1], tree[N//2])) #tree[1]:루트 값, tree[N//2]:N/2번 노드