import math
def palindrom(x): #펠린드롬 확인 함수
    global num 
    y = math.sqrt(x) #x의 제곱근 y, math.sqrt(i)는 제곱근을 구하는 수학함수
    x = list(map(int, str(x))) #회문 검사를 위해 리스트로 변환
    if x == x[::-1]: #x가 회문일 때
        if y.is_integer(): #x의 제곱근 y가 정수라면
            y = list(map(int, str(int(y)))) #y를 int(y)로 정수로 형변환 해주고 리스트로 변환 -> 정수로 형변환을 안해주면 실수형 '.'이 남아서 제대로 안됨
            if y == y[::-1]: #변환한 리스트 y도 회문이면
                num += 1 #개수 변수 +1

T = int(input()) #테스트 케이스
for i in range(T): 
    num = 0 #개수 세는 변수
    a, b = map(int, input().split()) #a부터 b까지 범위 지정

    for x in range(a, b+1): #a부터 b까지 
        palindrom(x) #펠린드롬 확인 함수 반복

    print('#{} {}'.format(i+1,num))

#x= int(math.sqrt(12))
#print(list(map(int, str(int(math.sqrt(12))))))