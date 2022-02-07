N = int(input()) #N까지 369 게임

for i in range(1, N+1):
    tsn = 0 #3,6,9가 들어있는 숫자를 세는 변수
    j = str(i) #문자열 카운트를 위해 i를 str로 형변환
    if '3' in j or '6' in j or '9' in j : #3,6,9가 문자 j에 포함되어있으면
        tsn += j.count('3') #3의 개수 세기
        tsn += j.count('6') #6의 개수 세기
        tsn += j.count('9') #9의 개수 세기

        for _ in range(tsn): #3,6,9가 포함된 개수만큼 '-'출력
            print('-', end='')
        print(' ', end='')
    else : #없으면 그대로 출력
        print(i, end=' ')

