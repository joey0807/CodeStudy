def involution(a,b): #거듭제곱 재귀함수
       if b == 1: #두번째로 입력받은 변수가 1이 될 때 까지 반복
           return a #결과값 리턴
       return involution(a,b-1)*a #두번째 변수를 -1 해주고 a*a


for _ in range(10): #테스트케이스 10개
    N = int(input()) 
    x, y = map(int,input().split()) #x^y 변수 값 입력


    print('#{} {}'.format(N,involution(x,y)))