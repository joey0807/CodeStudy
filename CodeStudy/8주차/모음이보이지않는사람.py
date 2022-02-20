T = int(input()) #테스트 케이스
for i in range(T):
    vowel = ['a','e','i','o','u'] #모음 리스트
    word = list(input()) #단어 입력
    new_word = word.copy() #입력받은 단어 복사

    for x in range(len(word)): #단어를 하나씩 비교
        for y in range(len(vowel)): #모음 리스트 전부와 비교
            if word[x] == vowel[y]: #만약 단어가 모음이라면
                new_word.remove(word[x]) #복사한 단어 리스트에서 모음을 제거
                  
    print('#{}'.format(i+1),end=' ') #줄바꿈을 하지 않고 공백 후 다음 출력
    print(*new_word, sep='') #정제된 단어를 공백 없이 출력
