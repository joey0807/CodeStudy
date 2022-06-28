t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())

    apart = []
    for x in range(k+1):
        h = []
        for y in range(1,n+1):
            if x == 0:
                h.append(y)
            else:
                h.append(sum(apart[x-1][:y]))
        apart.append(h)
    
    print(apart[k][n-1])