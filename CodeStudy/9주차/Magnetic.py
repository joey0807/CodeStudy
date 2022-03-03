for i in range(10): #테스트케이스 10개
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(N)] #리스트 입력
    num = 0 #개수 변수
    #N극=1, S극=2

    for x in range(99): #x축
        for y in range(100): #y축
            if mag[x][y] == 1: #n극이 있을때
                if mag[x+1][y] == 2: #s극이 옆에 있다면
                    num +=1 #개수 + 1
                elif mag[x+1][y] == 0: #없으면
                    mag[x+1][y] = mag[x][y] #한칸 이동
    
    print('#{} {}'.format(i+1, num))

            
