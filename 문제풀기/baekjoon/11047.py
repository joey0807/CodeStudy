n, m = map(int, input().split())
coin = []
count = 0

for i in range(n):
    money = int(input())
    coin.append(money)

for x in coin[::-1]:
    count += m//x
    m %= x

print(count)