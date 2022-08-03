t = int(input())
for _ in range(t):
    n = int(input())
    d = [0]*101

    d[1] = 1
    d[2] = 1
    d[3] = 1
    for i in range(98):
        d[i+3] = d[i] + d[i+1]

    print(d[n])