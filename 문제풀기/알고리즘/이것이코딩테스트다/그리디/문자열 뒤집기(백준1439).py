s = input()
result0 = 0 #전부 0으로 바꾸는 경우
result1 = 0 #전부 1로 바꾸는 경우

#첫 번째 원소에 대해 처리
if s[0] == '1': #첫 번째 원소가 1이면
    result0 += 1 #result0에 1 추가
else: #아니면
    result1 += 1 #result1에 1 추가

#두 번째 원소부터 전부 확인
for i in range(len(s)-1):
    if s[i] != s[i+1]: 
        if s[i+1] == '1': #다음 수에서 1로 바뀌는 경우
            result0 += 1
        else: #다음 수에서 0으로 바뀌는 경우
            result1 += 1

print(min(result0, result1)) #두 경우 중 최솟값 출력
