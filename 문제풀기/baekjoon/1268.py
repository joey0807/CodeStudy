n = int(input())
student = [] #학생별 속했던 반 리스트
same = [0]*n #같은 반이였는지 여부를 확인하는 리스트
ans = [] #학생 별 같은 반이였던 학생 수 리스트

for i in range(n):
    student.append(list(map(int,input().split())))
    same[i] = [0]*n

#print(len(student))
#new_student = list(map(list, zip(*student)))

for x in range(5): #1학년부터 5학년까지
    for y in range(n): #y번째 x학년
        for z in range(y+1,n): #z번의 x학년을 비교했을 때
            if student[y][x] == student[z][x]: #y번째 학생과 z번째 학생이 같은 반이였다면
                same[z][y] = 1 #same 값을 1로 바꿔줌
                same[y][z] = 1

for x in same: #same리스트에서
    ans.append(x.count(1)) #값이 1이였던 횟수 입력

print(ans.index(max(ans)) + 1) #1의 횟수가 가장 많은 학생이 임시 반장
