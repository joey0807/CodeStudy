#그래프
##함수
class Graph():
  def __init__(self,size):
    self.SIZE = size
    self.graph = [[0 for _ in range(size)] for _ in range(size)] #2차원 행렬 만들기

##전역
G = None

##메인
G = Graph(4) # 4x4 행렬 그리기
G.graph[0][1] = 1
G.graph[0][2] = 1
G.graph[0][3] = 1
G.graph[1][0] = 1
G.graph[1][2] = 1
G.graph[2][0] = 1
G.graph[2][1] = 1
G.graph[2][3] = 1
G.graph[3][0] = 1
G.graph[3][2] = 1


for row in range(4):
  for col in range(4):
    print(G.graph[row][col],end=' ') #2차원 행렬 출력
  print()