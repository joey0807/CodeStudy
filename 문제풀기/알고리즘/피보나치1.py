#리스트를 이용해서 구하기

n = int(input())

fibo = [0,1,]*n
for i in range(2,n+1):
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[n])
