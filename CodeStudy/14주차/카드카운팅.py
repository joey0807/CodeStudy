T = int(input())
for i in range(T):
    card = list(input()) #카드 정보

    card_list = [] #카드 정보를 구분해서 받을 리스트
    spade = 0 #스페이드 카드 개수
    dia = 0 #다이아몬드 카드 개수
    heart = 0 #하트 카드 개수
    clover = 0  #클로버 하트 개수

    for x in range(0,len(card),3): #card 문자열을 3개씩 나눠서 입력받음
        if card[x:x+3] not in card_list: #입력받는 card 문자열이 card_list에 없다면
            card_list.append(card[x:x+3]) #card_list에 추가
        else: #있다면 중복되는 거니까
            print('#{} ERROR'.format(i+1)) #에러 문구 출력하고
            break #멈춤
    else: #for-else문 : for문이 중간에 break로 끊기지 않고 수행되었을 때 수행하는 코드
        for x in card: #card 문자열을 비교
            if x == 'S': #S가 포함되어 있으면 스페이드 카드 개수 +1
                spade += 1 
            elif x == 'D': #D가 포함되어 있으면 다이아몬드 카드 개수 +1
                dia += 1
            elif x == 'H': #H가 포함되어 있으면 하트 카드 개수 +1
                heart += 1
            elif x == 'C': #C가 포함되어 있으면 클로버 카드 개수 +1
                clover += 1
            else: #나머지 문자열은 통과
                continue

        print('#{} {} {} {} {}'.format(i+1,13-spade,13-dia,13-heart,13-clover)) #계산된 카드 개수 출력