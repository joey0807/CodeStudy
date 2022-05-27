#금액 i를 만들 수 있는 최소한의 화폐 개수:a(i), 화폐 단위를 k라고 했을 때
#a(i-k)는 금액 (i-k)를 만들 수 있는 최소한의 화폐 개수
#a(i-k)를 만드는 방법이 존재하는 경우, a(i) = min(a(i),a(i-k)+1)
#존재하지 않는 경우, a(i) = 10001

n, m = map(int,input().split())

#n개의 화폐 단위 정보를 입력받기
array = []
for i in range(n):
    array.append(int(input()))

#한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j-array[i]]+1)

#계산된 결과 출력
if d[m] == 10001: #최종적으로 만드는 방법이 없는 경우
    print(-1) 
else:
    print(d[m])