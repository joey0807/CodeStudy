#왼쪽에 있는 수는 2로 나눠주고, 나머지는 버린다(1이 될 때 까지 반복)
#오른쪽에 있는 수는 2배를 해준다
#왼쪽에 있는 수가 홀수인 오른쪽의 수들을 모두 더해준다

def RussianPeasant(a, b):
    sum = 0
    while a != 0:
        if a%2 == 0:
            a = a//2
            b = b*2
        if a%2 != 0:
            sum += b
            a = a//2
            b = b*2
    return sum

x, y = map(int, input().split())
print(RussianPeasant(x,y))