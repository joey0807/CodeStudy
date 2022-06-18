n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

max_ans, min_ans = 0, 0

for x in first: #최대값이 되려면 전부 양수가 되면 됨
    if x < 0:
        max_ans += -x
    else:
        max_ans += x

for y in second: #최소값이 되려면 전부 음수가 되면 됨
    if y > 0:
        min_ans += -y
    else:
        min_ans += y

print(max_ans - min_ans)