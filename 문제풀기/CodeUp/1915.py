def A(a,b,N):
    if N > 0: #입력받은 N이 0이 될 때 까지
        a, b = b, a+b #피보나치 수열에 맞게 계산
        A(a,b,N-1) #계산 후 N--
    
    if N == 0: #N이 0이 됐다면
        print(a) #N번째의 숫자 출력

N = int(input())

A(0,1,N)
