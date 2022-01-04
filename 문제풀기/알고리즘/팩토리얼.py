#1부터 n까지의 곱 : 팩토리얼

n = int(input())
ans = 1
for i in range(1,n+1):
  ans = ans * i

print(ans)