T = int(input()) #테스트케이스

for i in range(T): 
    f_hour, f_minute, l_hour, l_minute = map(int, input().split()) #첫 번째 시, 첫 번째 분, 두 번째 시, 두 번째 분

    hour = f_hour + l_hour #시간 더해주기
    minute = f_minute + l_minute

    if minute > 59: #분이 60을 넘어간다면
        hour += 1 #시간 1 추가
        minute -= 60 #60을 빼줘서 분 보정
    
    if hour > 12: #시가 12를 넘어간다면
        hour -= 12 #12를 빼줘서 시 보정

    print('#{} {} {}'.format(i+1, hour, minute))