l = int(input())
s = input()
hash = 0

for x in range(l):
    #print(ord(x)-96,end=' ')
    hash += (ord(s[x])-96)*(31**x)

print(hash%1234567891)