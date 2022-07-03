n = int(input())
chart = []
rank = []
count = 1
for _ in range(n):
    weight, height = map(int, input().split())
    chart.append((weight, height))

for x in range(n):
    for y in range(n):
        if x != y:
            if chart[x][0] < chart[y][0] and chart[x][1] < chart[y][1]:
                count += 1
    rank.append(count)
    count = 1

print(*rank)