T = int(input()) #테스트케이스 개수
for i in range(T):
    p, q = map(float, input().split()) #확률 p, q

    s1 = (1-p)*q #s1 계산식
    s2 = p*(1-q)*q #s2 계산식

    print('#{}'.format(i+1),end=' ')

    if s1<s2:
        print('YES')
    else:
        print('NO')
