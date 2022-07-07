k, n = map(int, input().split())
line = []

for _ in range(k):
    x = int(input())
    line.append(x)

#cm = sum(line)//n -> 이분 탐색 안쓰고 단순 풀이

# for x in range(cm):
#     count = 0
#     for y in line:
#         count += y//cm

#     if count < n:
#         cm -= 1
#     else:
#         print(cm)
#         break

def binary(arr, num, start, end): #이분 탐색
    while start <= end:
        mid = (start+end)//2
        count = 0

        for x in arr:
            count += x//mid
        
        if count >= num:
            start = mid + 1
        else:
            end = mid - 1

    return end


print(binary(line,n,1,max(line)))