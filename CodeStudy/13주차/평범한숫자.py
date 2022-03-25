T = int(input()) 
for i in range(T):
    N = int(input()) 
    number = list(map(int, input().split())) #길이가 N인 리스트
    num = 0 #개수 세는 변수

    for x in range(1,N-1):
        check = number[x-1:x+2] #리스트를 3단위씩 끊기
        if check[1] != max(check) and check[1] != min(check): #끊은 리스트의 중간값이 그 리스트의 최대값이나 최소값이 아니면
            num += 1 #숫자 + 1

    print('#{} {}'.format(i+1,num))