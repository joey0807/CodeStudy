n, m = map(int,input().split())

A = [list(map(int, input().split())) for _ in range(n)] #n*m 행렬 A 입력
B = [list(map(int, input().split())) for _ in range(n)] #n*m 행렬 B 입력

#행렬 문자 하나씩 비교
for x in range(n):
    for y in range(m):
        print(A[x][y]+B[x][y],end=' ') #같은 위치에 있는 값 더하기
    print()