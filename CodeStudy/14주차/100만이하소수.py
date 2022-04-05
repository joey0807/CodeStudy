#에라토스테네스의 체 = 범위에서 합성수를 지우는 방식으로 소수를 찾음
#1. 1은 제거
#2. 지워지지 않은 수 중 제일 작은 숫자 2를 소수로 채택하고 나머지 2의 배수를 모두 지움
#3. 지워지지 않은 수 중 제일 작은 숫자를 소수로 채택하고 나머지 그 숫자의 배수를 모두 지우는 것을 반복

n=100
a = [False,False] + [True]*(n-1) #0과 1은 제외, 2부터 시작
primes=[] #소수를 저장할 빈 리스트

for i in range(2,n+1): #2부터 n까지
  if a[i]: #a[i]가 True라면
    primes.append(i) #소수니까 primes 리스트에 i 추가
    for j in range(2*i, n+1, i): #i를 소수로 채택했으니 i의 배수들을 모두 False로 바꿈
        a[j] = False
print(primes) #primes 리스트 출력