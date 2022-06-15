a,b = input().split()

#replace : 문자열 안에서 특정 문자를 새로운 문자로 변경하는 함수
#replace(old, new, [count])
#old : 현재 문자열에서 변경하고 싶은 문자
#new : 새로 바꿀 문자
#count : 변경할 횟수, 입력하지 않으면 old의 문자열 전체 변경
x = int(a.replace('6','5'))+ int(b.replace('6','5')) #모든 6을 5로 바꾸면 최소값
y = int(a.replace('5','6')) + int(b.replace('5','6')) #모든 5를 6으로 바꾸면 최대값

print(x, y)
