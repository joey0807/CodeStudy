def A(a,b):
    if a <= b: #a가 b보다 같거나 작을 때
        if a%2 == 1: #a가 홀수라면
            print(a, end=' ') #a 출력
        A(a+1,b) #a++


a, b = map(int, input().split())#a,b 입력
A(a,b)