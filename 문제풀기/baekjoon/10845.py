import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command[:5] == 'push ':
        x = int(command[5:])
        queue.append(x)

    elif command == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif command == 'size':
        print(len(queue))

    elif command == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif command == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif command == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])