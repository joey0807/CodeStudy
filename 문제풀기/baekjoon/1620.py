import sys

n, m = map(int, sys.stdin.readline().split())
dogam = {}

for i in range(1,n+1):
    p = sys.stdin.readline().rstrip()
    dogam[i] = p
    dogam[p] = i


for x in range(m):
    ans = sys.stdin.readline().rstrip()
    #isdigit() : 문자열이 숫자인지 판별하는 함수
    if ans.isdigit(): #ans가 숫자라면
        print(dogam[int(ans)]) #딕셔너리의 숫자에 맞는 value값 출력 
    else: #ans가 문자열이라면
        print(dogam[ans]) #딕셔너리의 value 값에 맞는 key 값 출력