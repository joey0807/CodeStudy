T = int(input()) #테스트케이스

for i in range(T): 
    N = int(input()) #돈 액수
    a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0 #오만원,만원,오천원,천원,오백원,백원,오십원,십원 개수 변수

    while N>=50000: #액수가 거슬러줘야 하는 돈보다 크다면 거슬러 줘야 하니까
        a += 1 #화폐 단위에 맞는 변수를 1씩 더해주고
        N -= 50000 #그 단위만큼 빼주는 것을 반복

    while N>=10000:
        b += 1
        N -= 10000

    while N>=5000:
        c += 1
        N -= 5000
        
    while N>=1000:
        d += 1
        N -= 1000
    
    while N>=500:
        e += 1
        N -= 500
    
    while N>=100:
        f += 1
        N -= 100
    
    while N>=50:
        g += 1
        N -= 50
    
    while N>=10:
        h += 1
        N -= 10
    
    print('#{}'.format(i+1))
    print('{} {} {} {} {} {} {} {}'.format(a,b,c,d,e,f,g,h))