# 간단한 수학적 아이디어를 이용해 더 효율적으로 푸는 법
# 반복되는 수열에 대해서 파악 -> (M / (K+1) * K) + (M % (K+1))
# 수열의 길이 = K+1, M이 K+1로 나누어 떨어지지 않을 때 = M % (K+1)
n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort() #입력받은 수 정렬
first = data[n-1] #가장 큰 수
second = data[n-2] #두번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m%(k+1)

result = 0
result += count*first #가장 큰 수 더하기
result += (m-count)*second #두번째로 큰 수 더하기

print(result)