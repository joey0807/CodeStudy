N = int(input()) #단어 개수
word_list = [] #입력받을 단어 리스트
word_cnt = [] #정렬될 단어 리스트

for i in range(N):
    word_list.append(input()) #단어 개수 만큼 입력받고 word_list에 저장

word = list(set(word_list)) #조건에 같은 단어가 여러 개 있으면 한 번만 출력하라 했으므로 set으로 정리

#word_list.sort(key=lambda x: len(x)) 처음 생각했던 문자 정렬 방법
for x in word: #word문자열 반복
    word_cnt.append((len(x),x)) #word 문자열의 문자 길이와 문자를 word_cnt 리스트에 저장

ans_word = sorted(word_cnt) #word_cnt 정렬

for x, y in ans_word: #정렬된 리스트 ans_word는 (x(문자길이),y(문자)) 형태로 저장돼 있으니
    print(y) #조건에 맞게 y(문자)만 줄바꿈하면서 출력