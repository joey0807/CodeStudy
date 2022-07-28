t = int(input())

fibo0 = [1,0,1]
fibo1 = [0,1,1]

def fibo(x):
    if x >= len(fibo0):
        for i in range(len(fibo0),x+1):
            fibo0.append(fibo0[i-1] + fibo0[i-2])
            fibo1.append(fibo1[i-1] + fibo1[i-2])

    print(fibo0[x], fibo1[x])

for _ in range(t):
    n = int(input())
    fibo(n)