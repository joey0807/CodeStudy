T = int(input())
for i in range(T):
    word = input() #문자열 입력받기

    for x in range(1,10): #마디 최대 길이는 10이니까 10까지
        #범위가 0부터 시작이면 문자열 비교가 안되니까 1부터 10까지
        if word[:x] == word[x:x*2]: #문자열 비교해서 같은 문자열이 반복되면
            break #그대로 반복문 그만두기
    print('#{} {}'.format(i+1,x)) #그만둔 시점의 x가 문자열의 길이