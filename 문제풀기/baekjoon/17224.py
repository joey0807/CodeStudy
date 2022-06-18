n, l, k = map(int, input().split())
level = []
score1, score2 = 0, 0

for i in range(n):
    normal, hard = map(int, input().split())
    level.append((normal, hard))

level1 = sorted(level, key = lambda x:x[1])
level2 = sorted(level)
# print(level1)
# print(level2)

for x in range(k):
    if level1[x][0] <= l:
        score1 += 100
    if level1[x][1] <= l:
        score1 += 40

for x in range(k):
    if level2[x][0] <= l:
        score2 += 100
    if level2[x][1] <= l:
        score2 += 40

print(max(score1, score2)) 