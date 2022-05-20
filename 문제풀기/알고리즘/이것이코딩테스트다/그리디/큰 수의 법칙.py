# 단순하게 푸는 답안
# m의 크기가 커진다면 시간 초과 판정
n, m, k = map(int, input().split()) #배열크기 n, 숫자가 더해지는 횟수 m, k

data = list(map(int, input().split())) #n개의 수 입력

data.sort() #입력받은 수들 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

result = 0

while True:
    for i in range(k): #가장 큰 수 k번 더하기
        if m == 0: #m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1 #더할 때마다 1씩 빼기
    
    if m == 0:
        break
    result += second #두 번째로 큰 수 한 번 더하기
    m -= 1 #더할 때마다 1씩 빼기

print(result)