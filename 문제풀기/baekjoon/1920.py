# 1. 집합 자료형 이용
# n = int(input())
# a = set(map(int, input().split())) #집합 자료형 set() 이용
# m = int(input())
# b = list(map(int, input().split()))

# for x in b:
#     if x in a:
#         print(1)
#     else:
#         print(0)

# 2. 이진 탐색 이용
def binary(array, target, start, end): # 이진 탐색 소스코드 구현
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a = list(map(int, input().split()))
a.sort()
m  = int(input())
b = list(map(int, input().split()))

for x in b:
    result = binary(a,x,0,n-1)
    if result != None:
        print(1)
    else:
        print(0)