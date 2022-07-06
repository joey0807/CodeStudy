k = int(input())
ans = []
for i in range(k):
    n = int(input())
    if n != 0:
        ans.append(n)
    else:
        ans.pop()

print(sum(ans))