for i in range(10): #테스트케이스 10개
    N = int(input()) #테스트케이스 번호 입력받음
    password = list(map(int, input().split())) #8개의 숫자 입력받음
    cycle = 1 #사이클 돌릴 때 증가하는 변수

    while True: #break 될 때 까지 반복
        cycle_password = password.pop(0) - cycle #첫 번째 숫자는 cycle만큼 감소되는 것이 반복됨

        if cycle_password < 0: #감소된 값이 음수면
            cycle_password = 0 #값은 0으로 유지

        password.append(cycle_password) #cycle만큼 감소된 값은 배열의 맨 끝으로 이동됨, 첫 번째 if문보다 앞에 있으면 마지막 숫자가 음수가 되는 경우가 발생함

        if cycle_password <= 0 : #cycle만큼 감소된 값이 0 이하라면
            break #반복문 종료

        cycle += 1 #cycle만큼 감소된 값이 0보다 크다면 cycle을 1 늘려서 반복

        if cycle > 5: #1부터 5만큼 감소시킨 후 뒤로 이동하는 사이클이므로
            cycle = 1  #cycle이 5를 넘어가면 다시 1로 초기화

    print('#{}'.format(i+1),end=' ')
    print(*password) #계산된 값 출력