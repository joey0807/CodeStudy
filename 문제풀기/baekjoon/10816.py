from collections import Counter #Counter 함수로 숫자 세기

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = [0]*m

counter = Counter(a) #a 리스트의 숫자 개수를 counter에 저장
#print(counter)

for x in range(m):
    if b[x] in counter:
        print(counter[b[x]],end=' ')
    else:
        print(0,end=' ')