n, m = map(int, input().split())
board = []
for _ in range(n):
    color = input()
    board.append(color)

ans = []

for x in range(n-7): #8*8 크기 고정이므로 -7을 해줘서 경우의 수 조절
    for y in range(m-7):
        black = 0 #검정색으로 칠하는 경우
        white = 0 #흰색으로 칠하는 경우
        for i in range(x,x+8): #8*8 크기 비교
            for j in range(y,y+8):
                if (i+j)%2 == 0: #행과 열의 인덱스 합이 짝수일 때와 홀수일 때의 색깔이 같음
                    if board[i][j] != 'W': #색깔을 비교했을 때 색깔이 다르면 그 색깔의 개수 +1
                        black += 1
                    if board[i][j] != 'B':
                        white += 1
                else:
                    if board[i][j] != 'B':
                        black += 1
                    if board[i][j] != 'W':
                        white += 1

        ans.append(black) #각각의 경우의 수의 합을 ans 리스트에 저장
        ans.append(white)

print(min(ans)) #경우의 수 최소값 출력