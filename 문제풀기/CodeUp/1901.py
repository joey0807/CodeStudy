def A(x,n): #재귀함수 A
    if x <= n: #x가 n보다 작거나 같다면
        print(x) #x출력
        A(x+1,n) #출력 후 x값 1 추가

n = int(input()) #n 입력

A(1,n) #1부터 n까지 출력이니까 x=1    