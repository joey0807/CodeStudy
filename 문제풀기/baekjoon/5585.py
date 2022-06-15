n = int(input())
coin = [500,100,50,10,5,1]
pay = 1000 - n
count = 0

for x in coin:
    count += pay//x
    pay %= x

print(count)