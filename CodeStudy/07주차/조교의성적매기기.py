T = int(input()) #테스트 케이스
for i in range(T):
    student, st_number = map(int, input().split()) #학생수 , 학점을 알고싶은 학생 번호
    report = [list(map(int, input().split())) for _ in range(student)] #성적 입력
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] #성적표
    std_grade = [] #총점을 입력받을 배열
    for x in range(student): #총점 계산하는 반복문
        total = ((report[x][0])*0.35) + ((report[x][1])*0.45) + ((report[x][2])*0.2) #총점 계산
        std_grade.append(total) #std_grade에 총점 입력

    #std_grade_sort = sorted(std_grade, reverse = True)
    std_grade_sort = std_grade.copy() #내림차순으로 점수가 높은 순서로 재배열 하기 위해 카피
    std_grade_sort.sort(reverse = True) #카피한 배열 내림차순

    # for y in range(student):
    #     if std_grade_sort[y] == std_grade[st_number-1]:
    #         print('#{} {}'.format(i+1,grade[y]))

    print('#{} {}'.format(i+1, grade[int(std_grade_sort.index(std_grade[st_number-1])/(student/10))])) 
    #학점을 알고 싶은 학생 번호의 점수가 있는 std_grade_sort 함수(점수를 정렬한 함수)의 인덱스 번호가 grade함수(성적 함수)와 같은 인덱스 번호면 그게 그 학생의 점수
    #N명의 학생이 있으면 N/10명의 학생들에게 동일한 평점을 부여할 수 있다고 조건에 있어서 student/10로 따로 계산