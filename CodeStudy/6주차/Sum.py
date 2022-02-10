for _ in range(10): #테스트케이스 10개 고정
    T = int(input()) #테스트케이스 번호 입력
    board = [list(map(int, input().split())) for _ in range(100)] #100x100 배열 입력
    sumList = [] #합을 저장하는 리스트
    
    for y in range(100): #100x100 배열이니 100번 반복
        row, col = [], [] #가로 세로 합
        cross1, cross2 = [], [] #왼쪽 위에서 시작하는 대각선, 왼쪽 아래에서 시작하는 대각선 합
        for x in range(100):
            row.append(board[y][x]) #가로줄의 합 입력
            col.append(board[x][y]) #세로줄의 합 입력
            if y == x: #x와 y가 같으면 왼쪽 위에서 시작하는 대각선
                cross1.append(board[y][x]) #대각선 합 입력
            if x == 99 - y: #x와 y가 99 차이나면 왼쪽 아래에서 시작하는 대각선
                cross2.append(board[y][99-x]) #대각선 합 입력
        sumList.append(max(sum(row), sum(col), sum(cross1), sum(cross2))) #합을 저장하는 리스트에 각 줄의 합의 최댓값을 입력받음
    
    print('#{} {}'.format(T, max(sumList))) #입력받은 값의 최댓값 출력