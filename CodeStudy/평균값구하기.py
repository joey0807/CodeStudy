#2071
T = int(input()) #테스트케이스 개수 입력받기

for i in range(T): #테스트케이스 개수 T만큼 반복
    arr = list(map(int, input().split())) #arr이라는 리스트에 공백을 구분으로 값을 입력
    ans = [num for num in arr] #ans에 arr리스트 값들을 저장

    #저장된 asn 값들을 sum으로 모두 더한 다음 10으로 나눔
    #10개의 수를 입력받아 평균값을 출력하므로 나누는 값이 10
    #소수점 첫째 자리에서 반올림한 정수임으로 round() 사용
    print('#{} {}'.format(i+1, round(sum(ans)/10)))