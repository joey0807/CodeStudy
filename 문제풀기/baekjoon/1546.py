n = int(input())
ans = 0
score = list(map(int,input().split()))

max_score = max(score)

for x in score:
    x = (x/max_score)*100
    ans += x

print(ans/n)