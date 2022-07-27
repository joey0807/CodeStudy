#특정 원소가 속한 집합 찾기
def find(arr, x):
    if arr[x] != x:
        arr[x] = find(arr, arr[x])
    
    return arr[x]

#두 원소가 속한 집합 합치기
def union(arr, x, y):
    x = find(arr, x)
    y = find(arr, y)
    if x < y:
        arr[y] = x
    else:
        arr[x] = y

n = int(input())
m = int(input())
computer = [0]*(n+1) #테이블 초기화

for i in range(1,n+1): #테이블을 자기 자신으로 초기화
    computer[i] = i

#union 연산 실행
for i in range(m):
    x, y = map(int, input().split())
    union(computer, x, y)

count = 0 
for x in range(2, n+1): #원소가 속한 집합 2부터 확인
    if find(computer,x) == 1: #속한 집합의 값이 1이라면
        count += 1 #1번과 연결된 것이니까 count에 1 추가

print(count)