T = int(input())
for i in range(T):
    N, A, B = map(int, input().split()) #N=총 인원수, A=P채널구독자, B=T채널 구독자
    gudok_max = 0 #최대 동시 구독자 수
    gudok_min = 0 #최소 동시 구독자 수

    gudok_max = min(A,B)

    if A+B > N:
        gudok_min = (A + B) - N

    else:
        gudok_min = 0

    print('#{} {} {}'.format(i+1,gudok_max, gudok_min))