n = int(input()) #데이터 개수 n
score = [] #정보를 받을 빈 리스트
for i in range(n):
    name, subject1, subject2, subject3 = input().split() #2차원리스트 형태로 이름, 3과목 점수들 입력
    score.append([name,int(subject1),int(subject2),int(subject3)])

sort_subject1 = sorted(score, key=lambda x: x[1], reverse=True) #첫 번째 과목을 기준으로 정렬
sort_subject2 = sorted(score, key=lambda x: x[2], reverse=True) #두 번째 과목을 기준으로 정렬
sort_subject3 = sorted(score, key=lambda x: x[3], reverse=True) #세 번째 과목을 기준으로 정렬

best_student = sort_subject1[0][0] #첫 번째 과목을 1등한 학생 이름
student_sub2 = sort_subject1[0][2] #첫 번째 과목을 1등한 학생의 두 번째 과목 점수
student_sub3 = sort_subject1[0][3] #첫 번째 과목을 1등한 학생의 세 번째 과목 점수

print(best_student,end=' ') #첫 번째 과목을 1등한 학생 이름 출력

for x in range(n): #데이터 개수만큼 반복
    if sort_subject2[x][2] == student_sub2: #두 번째 과목을 기준으로 정렬했을 때 학생의 두 번째 과목 점수와 같을 때 위치가 두 번째 과목의 석차 
        print(x+1,end=' ') #두 번째 과목의 석차 출력
        break #중복값이 있을 수 있으므로 break, 같은 점수가 있으면 가장 먼저 같을 때의 석차

for y in range(n):
    if sort_subject3[y][3] == student_sub3: #세 번째 과목을 기준으로 정렬했을 때 학생의 세 번째 과목 점수와 같을 때 위치가 세 번째 과목의 석차
        print(y+1) #세 번째 과목의 석차 출력
        break #마찬가지로 중복값이 있을 수 있으니 break