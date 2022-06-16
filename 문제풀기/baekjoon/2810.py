n = int(input())
chair = input()
couple = 0
count = n + 1

for x in chair:
    if x == 'L':
        couple += 1

if count - couple//2 > n:
    print(n)
else:
    print(count - couple//2)

    