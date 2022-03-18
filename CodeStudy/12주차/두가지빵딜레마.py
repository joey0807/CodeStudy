T = int(input()) #테스트케이스

for i in range(T):
    a,b,c = map(int, input().split()) #a, b = 빵 가격, c = 가지고 있는 돈
    num = 0 #살 수 있는 빵 개수

    if a>b: #a와 b를 비교해서 더 작은 값으로 몰아서 사는게 가장 많이 살 수 있음
        num = c//b

    else:
        num = c//a

    print('#{} {}'.format(i+1,num))