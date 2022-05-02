n = int(input()) #처리할 점수의 개수 n
score = list(map(int, input().split())) #처리할 점수 데이터 리스트 score
ans = [] #석차를 저장할 리스트 ans

for x in range(n):
    index = 1 #석차를 나타내는 변수 index, 1부터 시작
    for y in range(n):
        if score[x] < score[y]: #score의 x번째 값이 y번째 값보다 작다면
            index += 1 #index에 1 추가하는 것을 반복
    ans.append(index) #index의 총합을 ans에 추가

for x in range(n):
    print(score[x], ans[x])

