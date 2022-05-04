def A(n): #재귀함수 A
    if n > 0 : #n이 0보다 작을 때까지
        print(n) #n을 출력하고
        A(n-1) #n에서 1 빼주기

n = int(input()) #n 입력

A(n)   