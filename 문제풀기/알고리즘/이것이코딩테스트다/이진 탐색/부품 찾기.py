#이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None

n = int(input()) #가게 부품 개수 n
array = list(map(int, input().split()))
array.sort() #이진 탐색을 위해 정렬

m = int(input()) #손님이 확인 요청한 부품 번호 m
x = list(map(int, input().split()))

for i in x:
    #해당 부품이 존재하는지 확인
    result = binary_search(array,i,0,n-1)
    if result != None:
        print('yes',end=' ')
    else:
        print('no',end=' ')