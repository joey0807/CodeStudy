T = int(input())

for i in range(T):
    year = [31,28,31,30,31,30,31,31,30,31,30,31] #1년 날짜 리스트

    first_month, first_day, next_month, next_day = map(int, input().split()) #첫 번째 월, 첫 번째 날, 두 번째 월, 두 번째 날 입력

    if(first_month == next_month): #같은 달일 때
        total = next_day - first_day + 1
    
    if(first_month < next_month): #다른 달일 때
        total = (year[first_month-1]-first_day+1) + sum(year[first_month:next_month-1]) + next_day #첫 번째 달의 날짜 + 첫 번째와 두 번째 달 사이의 날짜 + 두 번째 날

    print('#{} {}'.format(i+1, total))
 