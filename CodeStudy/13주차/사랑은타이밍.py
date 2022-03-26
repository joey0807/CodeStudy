T = int(input())
for i in range(T):
    D, H, M = map(int, input().split()) #D일 H시 M분 입력

    realize = D*1440 + H*60+M #깨달아버린 시간을 분으로 계산
    day = 11*1440 + 11*60 + 11 #빼빼로 데이 시간을 분으로 계산

    if realize - day >= 0: #그 차이가 깨달음을 얻은 시간
        print('#{} {}'.format(i+1,realize - day)) #눈물의 시간 출력
    else: #음수면 약속 시간 전에 차임
        print('#{} {}'.format(i+1,-1)) #눈물의 -1 출력
