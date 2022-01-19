for i in range(10): #10개의 테스트케이스
    n = int(input()) #회문의 길이 입력
    palidom = [] #입력받을 행렬 초기화
    sum = 0 #총합의 개수를 입력받을 변수 sum
    for _ in range(8): #8x8 크기의 행렬 입력
        palidom.append(input())

    for x in range(8): #가로로 셀 때
        for y in range(9-n): #세로는 회문의 길이에 맞게 계산
            num = 1 #개수를 세는 변수
            word = palidom[x][y:y+n] #x번째 행의 y번째 열부터 회문의 길이만큼의 문장 입력받음
            if word == word[::-1]: #그 문장이 회문이면
                num *= 1 #num의 값은 1
            else:
                num *= 0 #회문이 아니면 num의 값은 0
            if num == 1:
                sum += 1 #num의 값이 1이면 그 문장은 회문이니까 총합 + 1

    for x in range(9-n): #세로로 셀 때
        for y in range(8): #반대로 가로를 회문의 길이에 맞게 계산
            num = 1 #똑같이 개수를 세는 변수
            word = '' #배열을 입력받는 변수를 *초기화* - 안해주니까 세로 계산이 제대로 안됨
            for z in range(x,x+n): #x번째 행부터 회문의 길이만큼 문자열을 저장
                word += palidom[z][y] #세로 계산은 범위만큼 인덱스 슬라이싱이 안되기 때문에 for문을 한번 더 중첩해서 행을 반복순회
            if word == word[::-1]:
                num *= 1
            else:
                num *= 0
            if num == 1:
                sum += 1

    print('#{} {}'.format(i+1, sum))
