T = int(input())
for i in range(T):
    n, m = map(int, input().split()) #n=뿔 개수, m=짐승 수

    # 유니콘과 트윈혼 마릿수 계산
    # unicorn + twinhorn = m
    # unicorn + twinhorn*2 = n

    twinhorn = n-m #계산 결과
    unicorn = m*2 - n

    print('#{} {} {}'.format(i+1,unicorn,twinhorn))
