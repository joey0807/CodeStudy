n = int(input())
milk = list(map(int, input().split()))
count = 0

for x in range(len(milk)):
    if milk[x] == count%3:
        count += 1      

print(count)