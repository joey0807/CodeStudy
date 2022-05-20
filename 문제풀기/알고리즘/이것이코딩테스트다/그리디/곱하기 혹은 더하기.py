s = input()
result = int(s[0]) #문자열의 첫 번째 숫자부터 시작

for i in range(1,len(s)): #문자열 두 번째부터 반복문 시작
    if int(s[i]) > 2: #숫자가 2보다 크면 곱하고
        result *= int(s[i])
    else: #2보다 작으면 더하기
        result += int(s[i])

print(result) #결과값 출력