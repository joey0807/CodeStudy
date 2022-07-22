import sys

m = int(sys.stdin.readline().rstrip())
s = []

for _ in range(m):
    command = sys.stdin.readline().rstrip()

    if command[:4] == 'add ':
        if int(command[4:]) in s:
            continue
        else:
            s.append(int(command[4:]))

    if command[:7] == 'remove ':
        if int(command[7:]) not in s:
            continue
        else:
            s.remove(int(command[7:]))

    if command[:6] == 'check ':
        if int(command[6:]) in s:
            print(1)
        else:
            print(0)

    if command[:7] == 'toggle ':
        if int(command[7:]) in s:
            s.remove(int(command[7:]))
        else:
            s.append(int(command[7:]))

    if command == 'all':
        s = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    if command == 'empty':
        s = []
