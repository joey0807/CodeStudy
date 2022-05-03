T = int(input())
for i in range(T):
    a, b = map(int,input().split())

    if a>b:
        print('#{} {}'.format(i+1,'>'))

    if a == b:
        print('#{} {}'.format(i+1,'='))

    if a < b:
        print('#{} {}'.format(i+1,'<'))