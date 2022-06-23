a, b = map(int, input().split()) #두 숫자 입력

#숫자를 리스트 형태로 변환
a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))

print(sum(a_list) * sum(b_list))