T = int(input())

for i in range(T):
    word = list(input())
    
    if word == word[::-1]:
        print('#{} {}'.format(i+1, 1))
    else:
        print('#{} {}'.format(i+1, 0))
    