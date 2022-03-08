T = int(input()) #테스트케이스 개수
for i in range(T):
    a = 1 #처음 시작 루트 1/1
    b = 1
    word = list(input()) #문자열 입력

    for x in word: #문자열 반복
        if x == 'L': #문자열이 L일 때
            a = a
            b = a+b
        
        if x == 'R': #문자열이 R일 때
            a = a+b
            b = b

    print('#{} {} {}'.format(i+1,a,b))
    