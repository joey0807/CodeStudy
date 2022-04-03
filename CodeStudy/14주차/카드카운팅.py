T = int(input())
for i in range(T):
    card = list(input())

    card_list = []
    spade = 0
    dia = 0
    heart = 0
    clover = 0

    for x in range(0,len(card),3):
        card_list.append(card[x:x+3])
        if card_list[-1] == card[x:x+3]:
            print('#{} ERROR')
        else:
            if card[x] == 'S':
                spade += 1
            elif card[x] == 'D':
                dia += 1
            elif card[x] == 'H':
                heart += 1
            elif card[x] == 'C':
                clover += 1

            
    #print('#{} {} {} {} {}'.format(i+1,13-spade,13-dia,13-heart,13-clover))

    # card1 = card[0:3]
    # card2 = card[3:6]
    # card3 = card[6:9]
    # card4 = card[9:]

    # if card1 == card2 or card1 ==card3 or card1 == card4 or card2 ==card3 or card2 == card4 or card3 == card4:
    #     print('#{} ERROR'.format(i+1))
    # else:
    #     for x in card:
    #         if x == 'S':
    #             spade += 1
    #         elif x == 'D':
    #             dia += 1
    #         elif x == 'H':
    #             heart += 1
    #         elif x == 'C':
    #             clover += 1
    #         else:
    #             continue
        
    #     print('#{} {} {} {} {}'.format(i+1,13-spade,13-dia,13-heart,13-clover))