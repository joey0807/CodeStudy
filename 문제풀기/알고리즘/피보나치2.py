#리스트 이용하지 않고
#변수 2개를 이용하기

n = int(input())

a=0
b=1

for i in range(n):
  a, b= b, a+b

print(a)