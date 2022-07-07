import sys
from collections import Counter

n = int(sys.stdin.readline().rstrip())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    arr.append(x)

arr_sort = sorted(arr)
count = Counter(arr_sort).most_common() #빈도가 많은 순서대로 정렬

#print(count)
maximum = count[0][1] #count의 value값이 최빈값의 개수
mode = [] #최빈값을 저장할 리스트
for x in count:
    if x[1] == maximum: #count 값이 maximum과 같으면 같은 최빈수
        mode.append(x[0])

#print(mode)

print(round(sum(arr)/n))
print(arr_sort[n//2])
if len(mode) > 1: #최빈수가 여러개면
    print(mode[1]) #그 중 두 번째로 작은 값 출력
else: #하나면
    print(mode[0]) #그 값 출력
print(max(arr)-min(arr))