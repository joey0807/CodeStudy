for i in range(10): #테스트케이스 10개
    N, pw = input().split() #문자열 입력
    new_pw = [] #새로 채워 넣을 문자열

    for x in pw: #문자열 pw 값을 하나씩 비교
        if new_pw and (new_pw[-1] == x): #문자열 new_pw의 마지막 값과 그 다음 들어오는 값이 같다면
            new_pw = new_pw[:-1] #new_pw 마지막 값 지우기
        else:
            new_pw += x #아니라면 값 추가

    print('#{}'.format(i+1), end=' ')
    print(*new_pw,sep='')
