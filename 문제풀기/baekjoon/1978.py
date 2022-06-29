n = int(input())
number = list(map(int, input().split()))
s = [False, False] + [True]*(1000)
primes = []
count = 0

for x in range(2, 1001):
    if s[x]:
        primes.append(x)
        for y in range(x*2,1001,x):
            s[y] = False

for i in number:
    if i in primes:
        count += 1

print(count)