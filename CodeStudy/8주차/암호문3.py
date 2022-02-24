def process(tp):
    global password
    if tp[0] == 'I':
        for x in range(len(tp[3:])):
            password.insert(int(tp[1])+x, tp[3+x])
    elif tp[0] == 'D':
        for _ in range(int(tp[2])):
            del password[int(tp[1])]
            if len(password) == int(tp[1]):
                break
    elif tp[0] == 'A':
        for x in range(int[tp[1]]):
            password.append(tp[2+x])

for i in range(10):
    N = int(input())
    password = list(input().split())
    cmdCount = int(input())
    cmd = list(input().split())

    temp = []
    cnt = 0
    for x in cmd:
        if x in ['I','A','D'] and len(temp) > 1:
            process(temp)
            temp = []
            temp.append(x)
        else:
            temp.append(x)

    print('#{} {}'.format(i+1,' '.join(password[:10])))