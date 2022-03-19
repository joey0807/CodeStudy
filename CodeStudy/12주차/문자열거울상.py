T = int(input()) #테스트케이스
for i in range(T):
    word = list(input()) #단어 입력

    word_reverse = word[::-1] #거울에 비추는게 조건이니까 문자열 뒤집기
    mirror = [] #거울에 비친 문자열

    for x in word_reverse: #뒤집은 문자열 반복문 
        if x == 'b': #b일땐 d
            mirror.append('d')
        if x == 'd': #d일땐 b
            mirror.append('b')
        if x == 'p': #p일땐 q
            mirror.append('q')
        if x == 'q': #q일땐 p
            mirror.append('p')

    print('#{}'.format(i+1),end=' ')
    print(*mirror,sep='')
        
