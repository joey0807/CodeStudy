n = int(input())
num = 1
count = 0

for x in range(1,n+1):
    num *= x

ans = list(map(int, str(num)))

for x in ans[::-1]:
    if x == 0:
        count += 1
    else:
        print(count)
        break