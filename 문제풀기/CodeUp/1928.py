def A(n): #우박수 함수
    if n == 1: #n이 1이 되면 과정이 끝났으니 리턴
        return

    elif n%2 == 1: #n이 홀수라면
        n = n*3 + 1 #3n+1
        print(int(n))
        A(n) #다시 우박수 함수 반복

    elif n%2 == 0: #n이 짝수라면
        n /= 2 #2로 나누기
        print(int(n))
        A(n) #다시 우박수 함수 반복

n = int(input())
print(n)
A(n)