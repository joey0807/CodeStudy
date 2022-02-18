def involution(a,b):
       if b == 1:
           return a
       return involution(a,b-1)*a


for _ in range(10):
    N = int(input())
    x, y = map(int,input().split())


    print('#{} {}'.format(N,involution(x,y)))