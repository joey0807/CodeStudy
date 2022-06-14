t = int(input()) #요리시간 t
s = [300,60,10] #버튼A:300초, 버튼B:60초, 버튼C:10초
count = 0 #개수를 셀 변수
a,b,c = 0,0,0 #각 버튼을 누른 횟수

for x in s:
    count += t//x #요리시간 t에서 s를 나눈 값을 count에 추가
    t %= x #요리시간 t에 s를 나눈 값의 나머지를 다시 t로 설정

    if x == 300: #이때 x가 300이면
        a += count #a버튼 누른 횟수 추가
    if x == 60: #x가 60이면
        b += count #b버튼 누른 횟수 추가
    if x == 10: #x가 10이면
        c += count #c버튼 누른 횟수 추가
    
    count = 0 #추가 후 초기화

if t != 0: #최종값 t가 0이 아니라면 시간을 정확히 맞출 수 없는 거기 때문에
    print(-1) #-1 출력
else: #t가 0이라면 정답 출력
    print(a,b,c)