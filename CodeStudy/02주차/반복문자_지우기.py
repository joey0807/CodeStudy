#반복문자 지우기(스택)

T = int(input()) #테스트 케이스 수

for i in range(T): #테스트 케이스 수만큼 반복
    arr = input() #입력할 문자열
    lst=[] #입력한 문자열을 받을 리스트
    for j in arr: #입력한 문자열 수 만큼 반복
        if lst and j == lst[-1]: #문자열이 같다면
            lst.pop() #삭제
        else:
            lst.append(j) #같다면 추가
    print('#{}'.format(i+1), len(lst)) #추가된 문자열의 길이 출력