#이진 탐색
def binary(data, start, end, k): #binary(이진탐색을 할 리스트, 리스트 첫 번째 값, 리스트 마지막 값, 리스트 값)
    while start <= end: #첫 번째 값이 마지막 값이 될 때 까지 반복
        mid = (start + end) // 2 #중간값 mid 선언
        if data[mid] == k: #리스트의 중간값이 찾아야 하는 값이라면
            return mid #그 값의 인덱스 값이 되는 mid 리턴
        elif data[mid] < k: #중간값이 찾아야 하는 값보다 작다면
            start = mid + 1 #첫 번째 값을 중간값 + 1로 설정
        else: #중간값이 찾아야 하는 값보다 크다면
            end = mid - 1 #마지막 값을 중간값 - 1로 설정

N = int(input()) #데이터 개수 N
data = list(map(int, input().split())) #데이터를 리스트로 입력받음
ans = [] #재정렬을 위한 빈 리스트

sort_data = sorted(data) #입력받은 데이터를 내림차순으로 정렬

for x in data: #입력받은 리스트를 기준으로 반복문
    ans.append(binary(sort_data,0,len(data)-1,x)) #이진탐색으로 찾은 값을 ans 리스트에 삽입


# for x in data:
    # for y in range(len(sort_data)):
        # if x == sort_data[y]:
            # print(y,end=' ') #시간초과 -> 이진 탐색으로 풀어야 시간초과가 되지 않음

print(*ans) #ans 리스트를 [] 없이 출력