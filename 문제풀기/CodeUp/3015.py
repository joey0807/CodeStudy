n, m = map(int, input().split()) #데이터 개수 n, 출력 인원 m
testscore = [] #이름과 점수를 저장할 빈 리스트
for i in range(n): 
    name, score = input().split() #이름과 점수 입력받고
    testscore.append([name,int(score)]) #2차원 배열 형태로 testscore리스트에 저장

sort_testscore = sorted(testscore, key=lambda x: x[1], reverse=True) #점수를 기준으로 오름차순 정렬된 sort_testscore

for x in range(m):
    print(sort_testscore[x][0]) #m개만큼 학생 이름 출력

