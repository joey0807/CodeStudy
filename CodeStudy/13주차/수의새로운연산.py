T = int(input())
for i in range(T):
    a, b = map(int, input().split()) #&(a), &(b)
    ans = 0 #정답

    line = [0]*300 #테스트케이스 숫자 크기만큼 배열을 크게 설정
    for l in range(300):
        line[l] = line[l-1]+l #(x,1)의 x값 

    x1 = 0 #첫번째 숫자의 x값
    y1 = 0 #첫번째 숫자의 y값
    x2 = 0 #두번째 숫자의 x값
    y2 = 0 #두번째 숫자의 y값

    for x in range(1, len(line)): #x축 따라 올라가다가
        if line[x] >= a: #x값이 a보다 크거나 같을때
            x1 = x - (line[x] - a) #x 좌표 값
            y1 = x - x1 + 1#y 좌표값
            break
    
    #예를 들어 a 값이 8(2,3)이라고 할때, line[x]가 8보다 커지는 경우는 line[x]가 10일때, 즉 x=4일때
    #y축 값이 하나씩 늘어나면서 x값은 하나씩 줄어듦
    #x축 값은 x값에서 line[x]와 a값의 차를 뺀 값, 즉 10에서 8을 뺀 숫자 2만큼 x축에서 뺀 값 4-2 = 2 
    #y축 값은 x값에서 x축값을 뺀 값인데, 좌표가 1부터 시작하니까 1을 더함, 즉 4에서 2를 뺀 2에서 1을 더해서 3
    #따라서 8은 (2,3)

    for y in range(1,len(line)): #두번째 값도 똑같이 계산
        if line[y] >= b:
            x2 = y - (line[y] - b)
            y2 = (y + 1) - x2
            break
    
    x3 = x1 + x2 #새롭게 정해지는 (x3, y3)
    y3 = y1 + y2

    ans = line[x3+y3-1] - (y3 - 1) #(x3,y3) 좌표 값

    #예를 들어 좌표 값이 (2,3)이라고 할 때, 계산을 하려면 먼저 계산 해놓은 line[]값을 찾아야 함
    #그 값은 x좌표 값과 y좌표 값의 합에서 1을 뺀 값, 즉 2+3-1 = 4
    #즉 line[4]일때, y좌표 값 - 1의 값만큼 뺀 값이 (2,3)의 값, 즉 8이 된다.        
    
    print('#{} {}'.format(i+1,ans))