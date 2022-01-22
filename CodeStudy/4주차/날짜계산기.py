T = int(input())

for i in range(T):
    year = [31,28,31,30,31,30,31,31,30,31,30,31]

    first_month, first_day, next_month, next_day = map(int, input().split())

    if(first_month == next_month):
        total = next_day - first_day + 1
    
    if(first_month < next_month):
        total = (year[first_month-1]-first_day+1) + sum(year[first_month:next_month-1]) + next_day

    print('#{} {}'.format(i+1, total))
 