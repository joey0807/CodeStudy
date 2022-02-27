T = int(input()) #테스트케이스
for i in range(T):
    N = int(input()) #나누는 인원 수

    print('#{}'.format(i+1),end=' ') 

    for _ in range(N):
        print('1/'+str(N),end=' ') 
    print()