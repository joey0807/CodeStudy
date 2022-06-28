n, k = map(int, input().split())

def F(x):
    ans = 1
    for i in range(1,x+1):
        ans *= i
    return ans

print(int(F(n)/(F(k)*F(n-k))))
