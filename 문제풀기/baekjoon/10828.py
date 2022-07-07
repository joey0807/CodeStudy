import sys #입력을 빠르게 받기 위한 함수
#input() => sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command[:5] == 'push ':
        x = int(command[5:])
        stack.append(x)

    elif command == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if not stack:
            print(1)
        else:
            print(0)

    elif command == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])