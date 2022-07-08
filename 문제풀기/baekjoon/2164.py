from collections import deque

n = int(input())
card = deque()
for x in range(n,0,-1):
    card.append(x)

while len(card) > 1:
    card.pop()
    card.appendleft(card[-1])
    card.pop()
    

print(card[0])