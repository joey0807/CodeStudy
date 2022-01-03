#2056
T = int(input()) #테스트케이스 개수 T

for i in range(T) : #테스트케이스만큼 반복

    year = str(input()) #년월일 입력받음, YYYYMMDD

    if int(year[4:6]) in [1, 3, 5, 7, 8, 10, 12]: #1, 3, 5, 7, 8, 10, 12월은 한 달이 31일
        if int(year[6:8]) >=1 and int(year[6:8]) <=31: #그래서 일이 1부터 31일 사이면
            print("#{} {}/{}/{}".format(i+1,year[0:4],year[4:6],year[6:8])) #YYYY/MM/DD 식으로 출력
        else:
            print("#{} {}".format(i+1,-1)) #아니면 -1 출력
 
    elif int(year[4:6]) in [4, 6, 9, 11]: #4, 6, 9, 11월은 한 달이 30일
        if int(year[6:8]) >=1 and int(year[6:8]) <=30: #위랑 같음
            print("#{} {}/{}/{}".format(i+1,year[0:4],year[4:6],year[6:8]))
        else:
            print("#{} {}".format(i+1,-1))
            
    elif int(year[4:6]) in [2]: #2월은 한 달이 28일
        if int(year[6:8]) >=1 and int(year[6:8]) <=28: #그래서 범위를 28까지
            print("#{} {}/{}/{}".format(i+1,year[0:4],year[4:6],year[6:8])) #나머지는 위와 같음
        else:
            print("#{} {}".format(i+1,-1))

    else:
        print("#{} {}".format(i+1,-1)) #위의 조건들이 성립하지 않으면 마찬가지로 -1 출력 
