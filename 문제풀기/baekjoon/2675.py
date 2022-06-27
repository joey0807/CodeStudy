t = int(input())

for i in range(t):
    r, s = input().split()
    for x in s:
        print(x*int(r),end='')
    print()