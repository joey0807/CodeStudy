T = int(input()) #테스트케이스
for i in range(T):
    N, Q = map(int, input().split()) #N : 상자 개수, Q : 반복할 횟수
    box = [0]*N #0으로 시작하는 빈 박스 N개 문자열

    for x in range(1,Q+1): #Q번 반복
        L, R = map(int, input().split()) #L번부터 R번까지 상자 숫자 변경 
        for y in range(L-1,R): #범위에 맞게 반복
            box[y] = x #그 범위 안의 문자열 값을 x로 변경

    print('#{}'.format(i+1), end=' ')
    print(*box)