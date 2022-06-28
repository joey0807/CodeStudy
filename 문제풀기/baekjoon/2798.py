n, m = map(int, input().split())
card = list(map(int, input().split()))
ans = []

for x in range(n):
    for y in range(1,n):
        for z in range(2,n):
            if x != y and x != z and y != z:
                count = card[x] + card[y] + card[z]
            if count <= m:
                ans.append(count)

print(max(ans))
