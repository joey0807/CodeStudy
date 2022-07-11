n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0 #이진 탐색 시작점
end = max(tree) #이진 탐색 끝점

ans = 0
while start <= end:
    total = 0
    mid = (start+end)//2

    for x in tree:
        if x > mid: #중간값으로 잘랐을 때의 길이 합
            total += x - mid
        
    if total < m: #길이의 합이 m보다 작으면
        end = mid - 1 #끝점 1 감소
    else: #길이의 합이 m보다 크다면
        ans = mid #최대한 덜 남기는게 정답이므로 ans에 값 입력
        start = mid + 1

print(ans)