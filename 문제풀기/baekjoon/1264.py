a = ['A','a','E','e','I','i','O','o','U','u'] #대,소문자 모음
b = 'a' #while문 반복을 위한 임의의 문자열
sum = 0 #모음 합 출력을 위한 변수

while b != '#': #입력받은 문자열이 #이 아니면 반복
    b = input() #문자열 입력
    if b != '#': #입력받은 문자열이 #이 아니면
        for x in b: #문자열을 하나씩 비교해서
            for y in range(len(a)):
                if x == a[y]: #모음이면 sum에 1 추가
                    sum += 1
        print(sum) #총합 출력 후
        sum = 0 #sum값 초기화