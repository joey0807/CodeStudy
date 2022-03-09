for i in range(10): #테스트케이스 10개
    T = int(input()) #테스트케이스 번호 입력
    palindrom = [] #입력할 문자열
    for _ in range(100):
        palindrom.append(input()) #100x100 문자열 입력

    def pld(string, length): #회문 길이 구하는 함수, pld(문자열, 문자열길이)
        max = length 
        while(length <= 100): #문자열 길이가 100이 될 때 까지 반복
            answer = 0 #종료 조건을 위한 변수 answer
            for x in range(100): #회문 구하는 반복문
                for y in range(101-length): #회문 길이에 맞게 계산
                    word = string[x][y:y+length] #회문인지 확인할 문자열
                    if word == word[::-1]: #회문이 맞다면
                        max = length #max 변수는 회문 길이 length
                        answer = 1 #1 더해서
                        break #회문 찾는 반복문은 그대로 종료
                if answer == 1:
                    break #answer가 1이 됐다는 것은 회문을 찾는 반복문이 종료됐다는 거니까 그대로 회문길이가 length일때의 반복문은 종료
            length += 1 #문자열 길이를 1 더해서 다시 반복
        return max #반복해서 나온 가장 큰 값을 max로 리턴

    row = pld(palindrom, 1) #가로줄 회문 길이 구하기

    palindrom2 = [] #세로줄일 때
    for x in range(100):
        list = "" #새로운 리스트
        for y in range(100):
            list += palindrom[y][x] #가로 세로 바꿔주고
        palindrom2.append(list) #새로운 리스트에 입력

    col = pld(palindrom2, 1) #세로줄 회문 길이 구하기

    print("#{} {}".format(T, max(row, col))) #총합해서 가장 큰 값 출력