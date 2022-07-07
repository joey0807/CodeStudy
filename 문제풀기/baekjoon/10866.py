from collections import deque
import sys

queue = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    command = sys.stdin.readline().rstrip()

    if command[:11] == 'push_front ':
        x = int(command[11:])
        queue.appendleft(x)

    elif command[:10] == 'push_back ':
        x = int(command[10:])
        queue.append(x)

    elif command == 'pop_front':
        if not queue:
            print(-1)

        else:
            print(queue[0])
            queue.popleft()
    
    elif command == 'pop_back':
        if not queue:
            print(-1)

        else:
            print(queue[-1])
            queue.pop()

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
