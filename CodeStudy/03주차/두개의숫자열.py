T = int(input())
for i in range(T):
    N, M = map(int, input().split()) 

    A = list(map(int, input().split())) #N개의 숫자로 구성된 숫자열 A
    B = list(map(int, input().split())) #B개의 숫자로 구성된 숫자열 B
    
    if N>M: #N이 작을 때의 기준으로
        N, M = M, N
        A, B = B, A
    
    sum = 0 #가장 높은 값을 저장할 변수
    for x in range(M-N+1): #작은 열과 더 많은 열을 돌릴 수 있는 최대의 수 = M-N+1
        temp = 0 #계산한 값을 저장할 변수
        for y in range(N): #작은 열의 길이에 맞춰서 반복
            temp += A[y] * B[y+x] #계산
    
        if temp > sum:
            sum = temp #각각의 값을 비교해서 최대값을 저장
    
    print('#{} {}'.format(i+1,sum))