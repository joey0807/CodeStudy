T = int(input())
for i in range(T):
    N = int(input()) #농장 크기
    total = 0 #총합
    farm = [list(map(int,input())) for _ in range(N)] #농장 테스트케이스 입력
    middle = N//2 #농장의 가운데 줄 - 절반 위쪽
    under_middle = middle #절반 아래쪽

    for x in range(N):
        for y in range(abs(middle-x), abs(N-under_middle)): #첫 줄은 N의 가운데부터 1칸, 다음 줄은 그 1칸 양옆에 1씩 더하는 식
            total += farm[x][y] #그 범위만큼 총합 더해주기

        if x < middle: #농장의 반절까지 아직 안왔다면
            under_middle = under_middle - 1 #절반이 되기 전까지 감소
        else:
            under_middle = under_middle + 1 #절반이 된 이후로는 증가

    print('#{} {}'.format(i+1,total))

