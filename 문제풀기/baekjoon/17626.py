import sys

n = int(sys.stdin.readline().rstrip())
d = [0]*(n+1)

d[1] = 1
# 규칙 :
# n보다 작은 제곱수를 찾고 n-제곱수를 인덱스를 가진 값에 1을 더해주면 됨
# => d[i-(j**2)] + 1
for i in range(2,n+1):
    minValue = 1e9
    j = 1

    while (j**2) <= i:
        minValue = min(minValue, d[i-(j**2)])
        j += 1

    d[i] = minValue + 1

print(d[n])
