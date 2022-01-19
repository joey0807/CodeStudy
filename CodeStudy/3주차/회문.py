for i in range(10):
    n = int(input())
    palidom = []
    sum = 0
    for _ in range(8):
        palidom.append(input())

    for x in range(8):
        for y in range(9-n):
            num = 1
            word = palidom[x][y:y+n]
            if word == word[::-1]:
                num *= 1
            else:
                num *= 0
            if num == 1:
                sum += 1

    for x in range(9-n):
        for y in range(8):
            num = 1
            word = ''
            for z in range(x,x+n):
                word += palidom[z][y]
            if word == word[::-1]:
                num *= 1
            else:
                num *= 0
            if num == 1:
                sum += 1

    print('#{} {}'.format(i+1, sum))
