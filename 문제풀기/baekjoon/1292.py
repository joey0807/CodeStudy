a, b = map(int, input().split()) #구간 시작 a, 구간 끝 b 입력
arr = [] #문제의 수열
#구간 끝 b까지의 범위에 맞게 문제 수열 채우기
for x in range(1,b+1):
    for y in range(1,x+1):
        arr.append(x)

ans = arr[a-1:b] #입력받은 구간으로 나누기

print(sum(ans)) #구간의 합 출력