n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #a는 오름차순
b.sort(reverse=True) #b는 내림차순

#첫 번째 인덱스부터 확인, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    if a[i] < b[i]: #a의 원소가 b 원소보다 작은 경우
        a[i], b[i] = b[i], a[i] #두 원소 교체
    else: #a의 원소가 크거나 같을 때 반복문 탈출
        break

print(sum(a))