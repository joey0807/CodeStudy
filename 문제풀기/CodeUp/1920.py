def A(n):
    #n이 0이나 1일 때
    if n < 1: #n이 0이라면
        return '0' #0 출력
    elif n == 1: #n이 1이라면
        return '1' #1 출력
    
    #n이 1보다 큰 숫자일 때
    if n%2 == 1: #n을 2로 나눈 나머지가 1이면
        return A(n//2) + '1' #n을 2로 다시 나누고 나머지 1을 결과값에 추가
    elif n%2 == 0: #n을 2로 나눈 나머지가 0이면
        return A(n//2) + '0' #n을 2로 다시 나누고 나머지 0을 결과값에 추가
    

n = int(input())

print(A(n)) #결과 출력
