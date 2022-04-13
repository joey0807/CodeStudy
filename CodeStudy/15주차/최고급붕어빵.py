T = int(input())
for i in range(T):
    n, m, k = map(int, input().split()) #n명 손님, m초에 k개 만듦
    customer = list(map(int, input().split()))#손님들이 도착하는 시간
    customer.sort() #도착 시간 정렬

    for x in range(n): #손님 수만큼 반복
        bread = (customer[x]//m) * k #손님이 입장한 시점에서 만들어진 빵의 개수

        if bread < x + 1: #그 빵의 개수가 손님 수보다 작으면
            print('#{} {}'.format(i+1,'Impossible')) #빵을 바로 제공하지 못하는 상황
            break
    else: #반복문이 끝날 때 까지 빵 개수가 손님 수보다 크다면
        print('#{} {}'.format(i+1,'Possible'))#제대로 제공이 가능함
    

    