T = int(input()) #테스트케이스 개수
m = [25,10,5,1] #거스름돈 종류

for i in range(T): 
    C = int(input()) #거스름돈 C
    count = 0
    a,b,c,d = 0,0,0,0

    for x in m:
        count += C//x
        C %= x
        #각각의 거스름돈의 개수 확인
        if x == 25:
            a += count
        if x == 10:
            b += count
        if x == 5:
            c += count
        if x == 1:
            d += count

        count = 0
    print(a,b,c,d)