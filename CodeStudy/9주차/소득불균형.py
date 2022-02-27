T = int(input()) #테스트케이스
for i in range(T):
    N = int(input()) #입력받을 정수 개수 N
    group = list(map(int, input().split())) #정수 입력
    num = 0 #카운트용 변수

    avg = sum(group)/N #입력받은 정수들의 평균

    for x in range(len(group)): #평균 이하의 숫자 개수를 세는 거니까
        if group[x] <= avg: #평균보다 작으면
            num += 1 #개수 카운트

    print('#{} {}'.format(i+1, num))