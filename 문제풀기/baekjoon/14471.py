n, m = map(int, input().split())
count, ans = 0, 0
point = []

for i in range(m):
    x, y = map(int, input().split())
    point.append((x,y))

point.sort(reverse=True)

for x in range(len(point)):
    if point[x][0] >= point[x][1]:
        count += 1
    else:
        ans += n - point[x][0]
        count += 1

    if count == m -1:
        break

print(ans)