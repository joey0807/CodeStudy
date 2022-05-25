from itertools import combinations #조합(Combinations) 라이브러리 사용

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c)) #일반 집
        elif data[c] == 2:
            chicken.append((r,c)) #치킨집

#모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

#치킨집 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0

    #모든 집에 대하여
    for hx, hy in house:
        #가장 가까운 치킨집을 찾기
        temp = 1e9 #1e9 = 10^9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        #가장 가까운 치킨집 까지의 거리 더하기
        result += temp
    return result

#치킨집 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)

