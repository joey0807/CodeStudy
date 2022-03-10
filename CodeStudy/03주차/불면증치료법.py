T = int(input()) #테스트케이스 T

for i in range(T): 
    N = int(input()) #N번 양
    lst = [0]*10 #0부터 9까지의 리스트 lst -> 0에서 9까지의 숫자가 나올 때 저장할 리스트
    k = 0 #몇번 반복했는지 확인하기 위한 변수 k

    while True: #리스트가 다 1로 찰 때까지 반복
        if 0 not in lst: #다 차서 0이 없으면
            break #반복 종료
        else: #그렇지 않다면
            k += 1 #1씩 추가
            kN = str(N*k) #kN을 문자열 형태로 저장
            for j in range(len(kN)): #kN의 길이만큼 반복하는데,
                lst[int(kN[j])] = 1 #설명하기 빡세네
                #N이 1295라면, 문자열로 저장한 1295의 길이는 4, kN은 문자열 형태이므로 1,2,9,5의 형태
                #4번 반복을 한다면, 반복문의 j는 0,1,2,3 형태
                #그래서 lst[kN[j]]라는 것은 kN의 1,2,9,5 값이 lst[1].lst[2],lst[9],lst[5] 형태가 되고, 거기에 1을 입력하는 형태로 반복
                #k값을 늘려가면서 lst 리스트를 채워나가고, lst가 다 1로 찼을 때 종료

    print('#{} {}'.format(i+1, kN))
    