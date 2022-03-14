T = int(input())
for i in range(T):
    N = int(input())
    card = list(map(str, input().split()))
    card_num = round(len(card)/2)

    new_card = []

    if len(card)%2==0:
        new_card1 = card[:card_num+1]
        new_card2 = card[card_num:]
        for x in range(card_num):
            new_card.append(new_card1[x])
            new_card.append(new_card2[x])
    
    if len(card)%2==1:
        new_card1 = card[:card_num+1]
        new_card2 = card[card_num+1:]
        for x in range(card_num):
            new_card.append(new_card1[x])
            new_card.append(new_card2[x])
        new_card.append(new_card1[-1])

    print('#{}'.format(i+1), end=' ')
    print(*new_card)
