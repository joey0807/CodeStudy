T = int(input()) #테스트케이스
for i in range(T):
    word = list(input()) #입력받을 문자열
    word_ans = [] #값을 담을 빈 문자열

    word.sort() #입력받은 문자열을 정렬해서 한번에 같은 값을 지우는 방식

    for x in word: 
        if word_ans and (word_ans[-1] == x): #값을 word_ans[]에 넣는데, 문자열 마지막 값과 넣을 값이 같다면
            word_ans = word_ans[:-1] #같이 없애버림
        else:
            word_ans += x #아니면 값 추가

    if len(word_ans) == 0: #문자열 값이 없다면
        print('#{} {}'.format(i+1, 'Good')) #Good 출력
    else: #아니면 문자열 값 출력
        print('#{}'.format(i+1), end=' ')
        print(*word_ans,sep='')