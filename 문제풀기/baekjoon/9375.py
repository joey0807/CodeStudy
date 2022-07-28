from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    fassion = []

    for i in range(n):
        x, y = input().split()
        fassion.append(y)

    fassion_count = Counter(fassion)

    count = 1
    for x in fassion_count:
        count *= fassion_count[x] + 1

    print(count - 1)