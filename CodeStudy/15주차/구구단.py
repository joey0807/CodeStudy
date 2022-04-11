T = int(input())
for i in range(T):
    n = int(input()) #숫자 입력
    gugu = [] #n의 약수 저장 리스트
    for x in range(1,n+1): #n의 약수를 구해서
        if n%x == 0:
            gugu.append(x) #gugu 리스트에 저장
            
    if len(gugu)%2 == 0: #약수의 개수가 짝수일 때
        if gugu[len(gugu)//2-1]*gugu[len(gugu)//2] == n and gugu[len(gugu)//2] < 10: #두 중간값의 곱이 n이고 그 둘 중 큰 수가 10보다 작으면 조건 성립
            print('#{} {}'.format(i+1,'Yes'))
        else:
            print('#{} {}'.format(i+1,'No'))    
    else: #약수의 개수가 홀수일 때
        if gugu[(len(gugu)//2)]**2 == n and gugu[(len(gugu)//2)] < 10 : #중간값의 제곱 값이 n이고 그 값이 10보다 작으면 조건 성립
            print('#{} {}'.format(i+1,'Yes'))
        else:
            print('#{} {}'.format(i+1,'No'))
