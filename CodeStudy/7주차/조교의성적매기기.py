T = int(input())
for i in range(T):
    student, st_number = map(int, input().split())
    report = [list(map(int, input().split())) for _ in range(student)]
    grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    std_grade = []
    for x in range(student):
        total = ((report[x][0])*0.35) + ((report[x][1])*0.45) + ((report[x][2])*0.2)
        std_grade.append(total)

    std_grade_sort = sorted(std_grade, reverse = True)

    #print(std_grade)

    #want_grade = ((report[st_number-1][0])*0.35) + ((report[st_number-1][1])*0.45) + ((report[st_number-1][2])*0.2)
    
    for y in range(student):
        if std_grade_sort[y] == std_grade[st_number-1]:
            print('#{} {}'.format(i+1,grade[y]))