T = int(input()) #테스트케이스
for i in range(T):
        N, M = map(int, input().split()) #N*N크기의 배열, M*M크기의 파리채

        flies = [list(map(int, input().split())) for _ in range(N)] #N*N크기의 배열 입력받기
        maxsum = 0 #총합 변수

        for x in range(N-M+1): #N*N크기의 배열 안에서 M*M크기의 배열이 움직일 수 있는 범위
            for y in range(N-M+1): 
                kill = 0 #파리채 배열의 합 변수
                for dx in range(M): #파리채 배열의 반복문
                        for dy in range(M):
                                kill += flies[x+dx][y+dy]  #파리채 배열 안의 값 더하기
                                if kill > maxsum: #더한 값이 최댓값이라면
                                        maxsum = kill #총합 갱신

        print('#{} {}'.format(i+1,maxsum))
