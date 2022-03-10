T = int(input())
for i in range(T):
    N, K = map(int, input().split()) #단어 퍼즐 크기 N, 단어 길이 K
    puzzle = [list(map(int,input().split())) for _ in range(N)] #퍼즐 문자열
    total = 0 #총합을 나타내는 변수

    for x in range(N):
        count = 0 #빈 칸을 세는 변수
        for y in range(N): #가로(행) 방향 찾기
            if puzzle[x][y] == 1: #1이 빈 칸을 나타냄
                count += 1 #빈칸이면 하나 카운트
            if puzzle[x][y] == 0 or y == N-1: #빈 칸이 아니거나 문자열 끝에 왔을 때
                if count == K: #카운트한 빈 칸이 단어길이 K와 같다면
                    total += 1 #총합 + 1
                count = 0 #다음 행으로 넘어가서 찾기 전에 초기화

        for y in range(N): #세로(열) 방향 찾기
            if puzzle[y][x] == 1: #행렬 위치만 바꿔주고 나머지는 동일
                count += 1
            if puzzle[y][x] == 0 or y == N-1:
                if count == K:
                    total += 1
                count = 0

    print('#{} {}'.format(i+1,total))