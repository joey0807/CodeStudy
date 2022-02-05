T = int(input()) #테스트케이스

for i in range(T): 
    N = int(input()) #2차원 배열 크기

    snail = [[0 for _ in range(N)] for _ in range(N)] #N*N 크기의 0으로 채워진 2차원 배열 만들기
    dx = [0,1,0,-1] #행 좌표를 결정할 배열
    dy = [1,0,-1,0] #열 좌표를 결정할 배열
    d = 0 #dx, dy 배열값을 가리킬 변수
    x = 0 #행 좌표
    y = 0 #열 좌표
    num = 1 #입력은 1부터 시작

    while(1): #break가 될 때 까지 반복
        if num == N*N+1: #입력한 num 값이 N*N 2차원 배열의 크기보다 커진다면
            break #함수 종료

        if -1<x<N and -1<y<N and snail[x][y] == 0: #행과 열의 크기가 N을 넘지 않고, 아직 num 값이 입력되지 않았다면
            snail[x][y] = num #2차원 배열의 값이 num 값이 되고
            x += dx[d] #행과 열(x와 y)의 위치를 재정의
            y += dy[d]
            num += 1 #num값을 1씩 더해가며 입력

        else: #범위를 넘어섰다면
            x -= dx[d] #넘어간 범위를 다시 되돌리고
            y -= dy[d]
            d += 1 #dx와 dy의 배열 값을 바꿔줌으로써 진행 방향을 바꿔줌

            if d>3: #d의 값이 dx, dy 배열 크기보다 커진다면
                d %= 4 #dx, dy 배열 크기가 4이므로 4의 나머지값으로 재조정
            
            x += dx[d] #바뀐 dx, dy 값으로 행과 열(x와 y) 값 설정
            y += dy[d]
            snail[x][y] = num #다시 값 입력하고 반복
            num += 1
            x += dx[d] 
            y += dy[d]

            #dx, dy의 값이 교차해 가면서 달팽이 껍질 모양처럼 회전하면서 배열을 채우게 됨
            #y좌표만 움직이다가 y 좌표 범위가 넘어가게 되면 y값을 멈추고 x좌표만 움직이고
            #x좌표만 움직이다 x좌표 범위가 넘어가게 되면 x값을 멈추고 다시 y좌표룰 움직임
            #dx=[0,1,0,-1]이고, dy=[1,0,-1,0]이므로 1씩 더해지면서 왼쪽으로 가고 밑으로 가면서 진행하다 
            #-1씩 더해지면서 반대로 오른쪽으로 가고 위로 가면서 진행되는 것이 반복됨 

    print('#{}'.format(i+1))

    for a in range(N): #그렇게 진행된 배열 값을 str 형태로 출력
        ans = ''
        for b in range(N):
            ans += str(snail[a][b])+' '
        print(ans)