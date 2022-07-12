t = int(input())

def gcd(x,y): #최대 공약수(유클리드 호제법)
    while y > 0:
        x, y = y, x%y

    return x

for _ in range(t):
    a, b = map(int, input().split())
    print(a*b//gcd(a,b)) #최소공배수는 a와 b의 곱을 a,b의 최대 공약수로 나누면 나옴