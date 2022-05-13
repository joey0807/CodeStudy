a, b, c = map(int, input().split()) #a,b,c 입력

for x in range(min(a,b,c),0,-1): #a,b,c 최소 공배수
    if a%x==0 and b%x==0 and c%x==0:
        print(x)
        break