def A(n):
    global m
    if n > 0: #n이 0보다 크다면
        m *= n #m*n 후
        A(n-1) #n--


n = int(input())
m = 1 #팩토리얼 계산을 위한 변수 m
A(n)
print(m)