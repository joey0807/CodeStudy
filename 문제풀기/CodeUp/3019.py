n = int(input()) #데이터 개수 n
schedule = [] #스케줄 입력받을 리스트
for i in range(n):
    name, y, m, d = input().split() #스케줄명, 연, 월, 일 입력
    schedule.append([name,int(y),int(m),int(d)]) #입력받은 값을 저장

sort_schedule = sorted(schedule, key=lambda x: (x[1],x[2],x[3],x[0]), reverse=False)
#reverse=False -> 오름차순으로 정렬
#1. x[1] : 연도를 기준으로 오름차순 정렬
#2. x[2] : 월을 기준으로 오름차순 정렬
#3. x[3] : 일을 기준으로 오름차순 정렬
#4. x[0] : 날짜가 동일할 경우 사전 순서로 오름차순 정렬

for x in range(n):
    print(sort_schedule[x][0]) #정렬된 데이터의 스케쥴명 출력