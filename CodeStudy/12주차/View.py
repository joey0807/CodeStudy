for i in range(10): #테스트케이스 10개
    n = int(input()) #테스트케이스 길이
    building = list(map(int, input().split())) #빌딩 층수
    num = 0 #조망권이 확보되는 칸 수

    for x in range(2,n-2): 
        b_left1 = building[x] - building[x-1] #빌딩 왼쪽 한 칸
        b_left2 = building[x] - building[x-2] #빌딩 왼쪽 두 칸
        b_right1 = building[x] - building[x+1] #빌딩 오른쪽 한 칸
        b_right2 = building[x] - building[x+2] #빌딩 오른쪽 두 칸

        if b_left1 >0 and b_left2 >0 and b_right1 >0 and b_right2 >0: #하나라도 계산이 음수가 나오면 조망권이 확보되지 않음
            num += min(b_left1,b_left2,b_right1,b_right2) #네 값 중에서 가장 작은 값이 조망권이 확보되는 칸 수

    print('#{} {}'.format(i+1,num))