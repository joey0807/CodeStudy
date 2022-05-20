n, m = map(int, input().split()) #볼링공 개수 n, 공 최대무게 m
ball = list(map(int,input().split())) #공 무게 값 입력
ball.sort()

#1부터 10까지 무게를 담을 수 있는 리스트
arr = [0] * 11 #m은 최대 10까지가 문제 조건

for x in ball:
    arr[x] += 1 #각 무게에 해당하는 볼링공의 개수 카운트

result = 0

for i in range(1,m+1): #1부터 m까지 각 무게에 대해 처리
    n -= arr[i] #무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += arr[i]*n #b가 선택하는 경우의 수와 곱하기

print(result)
