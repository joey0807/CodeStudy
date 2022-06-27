t = int(input())
count = 1
ans = 0

for i in range(t):
    quize = input()
    for x in quize:
        if x == 'O':
            ans += count
            count += 1
        else:
            count = 1

    print(ans)
    count = 1
    ans = 0