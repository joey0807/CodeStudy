T = int(input()) #테스트케이스 개수

for i in range(T):
    a, b, c = map(int, input().split()) #직사각형 세 변 길이 입력
    d = 0 #나머지 한 변 길이

    if a == b: # a와 b가 같다면
        d += c #나머지 한 변 길이는 c
    
    elif a == c: #a와 c가 같다면
        d += b #나머지 한 변 길이는 b

    else: #그것도 아니라 b와 c가 같다면
        d += a #나머지 한 변 길이는 a, 입력으로 직사각형이 불가능한 경우는 주어지지 않는다 했으니 나머지는 고려 x
    
    print('#{} {}'.format(i+1, d))