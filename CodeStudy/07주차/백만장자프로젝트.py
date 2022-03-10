T = int(input()) #테스트케이스
for i in range(T):
    N = int(input()) #입력할 숫자 N개
    money = 0 #사재기로 번 돈
    future = list(map(int,input().split())) #매매가 리스트

    max = future[-1] #리스트의 마지막값 -> 최대값으로 설정해서 비교

    for x in range(len(future)-1,-1,-1): #리스트를 거꾸로 돌려서 비교
        if max > future[x]: #리스트 값이 최대값보다 크다면
            money += max - future[x] #사재기한걸 팔아야 할 때이므로 계산해서 번 돈 변수에 추가
        else: #아직 크지 않다면
            max = future[x] #아직은 매수 타이밍
    
    print('#{} {}'.format(i+1, money))


