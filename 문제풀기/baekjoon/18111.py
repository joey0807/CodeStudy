import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
time = sys.maxsize

#0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    #블록 확인
    for x in range(n):
        for y in range(m):
            #블록이 층 수보다 더 크다면
            if ground[x][y] >= target:
                max_target += ground[x][y] - target

            #블록이 층 수보다 더 작다면
            else:
                min_target += target - ground[x][y]

    #인벤토리에 있는 총 블록 수 = 현재 인벤토리에 있는 블록 + max_target
    if max_target + b < min_target: #전부 채울 수 없으니 패스
        continue
    
    #블록제거와 블록 추가 : min_target + (max_target * 2)
    if min_target + (max_target*2) <= time: #높이를 오름차순으로 탐색하기 때문에 걸린 시간이 같아도 더 높은 높이가 출력됨
        time = min_target + (max_target*2)
        height = target

print(time, height)