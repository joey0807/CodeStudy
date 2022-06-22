n = input()
count = 0
for x in n:
    print(x,end='')
    count += 1
    if count == 10:
        print()
        count = 0