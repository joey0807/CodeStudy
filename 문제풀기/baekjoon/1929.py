m, n = map(int, input().split())

a = [False,False] + [True]*(n-1) #0과 1은 제외, 2부터 시작
primes=[] #소수를 저장할 빈 리스트

for i in range(2,n+1): #2부터 n까지
  if a[i]: #a[i]가 True라면
    primes.append(i) #소수니까 primes 리스트에 i 추가
    for j in range(2*i, n+1, i): #i를 소수로 채택했으니 i의 배수들을 모두 False로 바꿈
        a[j] = False

#print(*primes) #primes 리스트 출력

for x in primes:
    if x>=m:
        print(x)

