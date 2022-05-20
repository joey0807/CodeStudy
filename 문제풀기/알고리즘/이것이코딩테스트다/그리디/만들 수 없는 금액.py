n = int(input())
coin = list(map(int, input().split()))
coin.sort()

ans = 1

for i in coin:
    if ans < i: #ans가 i값보다 작으면 더이상 만들 수 없는 값이므로
        break #함수 종료
    else:
        ans += i

print(ans)