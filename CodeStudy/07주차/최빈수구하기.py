T = int(input()) #테스트케이스
for i in range(T):

    t = int(input()) #테스트케이스 번호 입력

    math_score = [0 for _ in range(101)] #수학 점수 배열
    student = list(map(int, input().split())) #학생 점수 입력
    max_score = 0 #수학 점수 배열의 최대값
    max_index = 0 #수학 점수 배열 최대값의 인덱스
    

    for x in range(len(student)): #학생 점수를 입력받고
        math_score[student[x]] += 1 #그 학생 점수 숫자가 수학 점수 배열의 인덱스 번호가 되고, 그 칸에 +1
    
    for y in range(101): #총 0점부터 100점이므로
        if math_score[y] >= max_score: #수학 점수 배열의 가장 높은 값이 최대값보다 크거나 같다면
            max_score = math_score[y] #값 갱신
            max_index = y #인덱스 값 저장

    #print('#{} {}'.format(i+1, math_score.index(max(math_score))))
    #index 함수는 같은 값인 경우 최소값을 나타내기 때문에 조건과 안맞음
    print('#{} {}'.format(i+1,max_index))