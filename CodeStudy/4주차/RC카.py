T = int(input())
for i in range(T):
    N = int(input()) #입력받을 커맨드 개수 N
    total = 0 #총 이동한 거리
    speed = 0 #커멘드로 입력받을 속도

    for j in range(N): 
        rc = input().split() #문자열 형태로 커멘드 입력받음, [커맨드, 속도]
                             #0 : 현재속도 유지, 1 : 가속, 2 : 감속

        if int(rc[0]) == 0: #입력받은 커멘드가 0일때
            speed = speed #속도 유지
            total += speed
        
        elif int(rc[0]) == 1: #입력받은 커멘드가 1일때
            speed += int(rc[1]) #속도 더해주기
            total += speed

        elif int(rc[0]) == 2: #입력받은 커멘드가 2일때
            if int(rc[1]) >speed: #입력받은 속도가 현재 속도보다 크다면
                speed = 0 #속도는 0이 되고 이동한 거리는 그대로
                total = total
            else: #입력받은 속도가 현재 속도보다 작다면
                speed -= int(rc[1]) #현재속도에서 입력받은 속도를 빼고 계산
                total += speed 

    print('#{} {}'.format(i+1, total))