n = int(input())
name = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
players = [0]*26
count = 0

for x in range(n):
    player = input()
    for y in range(len(name)):
        if name[y] == player[0]:
            players[y] += 1

if max(players) >= 5:
    for y in range(len(players)):
        if players[y] >= 5:
            print(name[y],end='')
else:
    print('PREDAJA')