T = int(input())
for i in range(T):
    test_case = list(map(int, input().split()))

    print('#{} {}'.format(i+1,max(test_case)))