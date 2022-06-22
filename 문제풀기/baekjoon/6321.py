n = int(input())
program = []
for i in range(n):
    computer = input()
    program.append(computer)

for x in range(n):
    print(f'String #{x+1}')
    for y in program[x]:
        if y == 'Z':
            print('A',end='')
        else:
            print(chr(ord(y)+1),end='')
    print('\n')