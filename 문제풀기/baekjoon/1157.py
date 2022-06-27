from collections import Counter #딕셔너리 속도 단축

s = input()
count = 0

upper_s = s.upper() #알파벳을 전부 대문자로 변환

# for x in upper_s:
#     ans[x] = upper_s.count(x) -> 너무 오래걸려

ans = Counter(upper_s) #Counter함수로 입력받은 단어의 알파뱃 개수 딕셔너리 생성

#max_ans = max(ans, key=ans.get)
max_ans = max(ans.values()) #딕셔너리의 value 최대값
#print('max_ans : ',max_ans)

for key, value in ans.items(): #최대값이 여러개인지 확인하는 반복문
    if value == max_ans:
        count += 1

if count > 1: #같은 최대값이 여러개면 '?' 출력
    print('?')
else:
    print(max(ans, key=ans.get)) #같은 최대값이 없으면 딕셔너리의 최대값을 가지는 key값 출력