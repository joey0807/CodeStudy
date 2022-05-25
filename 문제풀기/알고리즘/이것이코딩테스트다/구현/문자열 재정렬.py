s = input() #문자열 입력
result = [] #결과값 저장할 리스트
value = 0 #숫자를 더한 값을 저장할 변수

for x in s:
    if x.isalpha(): #원소가 알파벳이면
        result.append(x) #result에 저장
    else: #숫자라면
        value += int(x) #value에 값 더하기 

result.sort() #알파벳 정렬

if value != 0: #숫자값이 있다면
    result.append(str(value)) # result 끝에 값 추가

print(''.join(result))