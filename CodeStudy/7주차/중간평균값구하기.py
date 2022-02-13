T = int(input()) #테스트케이스
for i in range(T):
    array = list(map(int, input().split())) #숫자 10개 입력

    array_max = max(array) #입력받은 숫자들 중 최대값
    array_min = min(array) #입력받은 숫자들 중 최소값

    #print(array_max, array_min)
    ans = (sum(array) - (array_max + array_min)) / 8 #최대 수와 최소 수를 제외한 나머지 평균값 계산

    print('#{} {}'.format(i+1,round(ans)))