a = input() #문자열 입력

for x in a: #문자를 하나씩 비교
    if x.isupper() == True: #문자가 대문자면
        print(x.lower(),end='') #소문자로 출력
    else: #문자가 소문자라면
        print(x.upper(),end='') #대문자로 출력

#string.upper() : 문자열 객체 string을 대문자로 변환
#string.lower() : 문자열 객체 string을 소문자로 변환
#string.isupper() : 문자열 객체 string의 모든 문자가 대문자인지 검사
#string.islower() : 문자열 객체 string의 모든 문자가 소문자인지 검사