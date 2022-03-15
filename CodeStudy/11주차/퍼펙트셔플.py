T = int(input()) #테스트케이스 개수
for i in range(T):
    N = int(input()) #입력받을 문자 개수
    card = list(map(str, input().split())) #문자 입력
    card_num = len(card)//2 #문자 개수/2의 정수값

    new_card = [] #셔플해서 새로 만들 리스트

    if len(card)%2==0: #개수가 짝수일 때
        new_card1 = card[:card_num+1] 
        new_card2 = card[card_num:] #입력받은 문자를 절반으로 나눠줌
        for x in range(card_num):
            new_card.append(new_card1[x]) 
            new_card.append(new_card2[x]) #번갈아 가면서 빈 리스트에 값 삽입
    
    if len(card)%2==1: #개수가 홀수일 때
        new_card1 = card[:card_num+1]
        new_card2 = card[card_num+1:] #홀수일 때는 교대로 먼저 놓는 쪽이 한 장 더 많음
        for x in range(card_num):
            new_card.append(new_card1[x])
            new_card.append(new_card2[x]) #번갈아 가면서 빈 리스트에 값 삽입
        new_card.append(new_card1[-1]) #한 장 더 들어가는 값 삽입

    print('#{}'.format(i+1), end=' ')
    print(*new_card)