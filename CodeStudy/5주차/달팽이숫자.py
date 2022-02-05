T = int(input())

for i in range(T):
    N = int(input())

    snail = [[0 for _ in range(N)] for _ in range(N)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    d = 0
    x = 0
    y = 0
    num = 1

    while(1):
        if num == N*N+1:
            break

        if -1<x<N and -1<y<N and snail[x][y] == 0:
            snail[x][y] = num
            x += dx[d]
            y += dy[d]
            num += 1

        else:
            x -= dx[d]
            y -= dy[d]
            d += 1

            if d>3:
                d %= 4
            
            x += dx[d]
            y += dy[d]
            snail[x][y] = num
            num += 1
            x += dx[d]
            y += dy[d]

    print('#{}'.format(i+1))

    for a in range(N):
        ans = ''
        for b in range(N):
            ans += str(snail[a][b])+' '
        print(ans)