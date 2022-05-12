a ,b = map(int, input().split()) #두 숫자 a,b 입력

#최대공약수 구하기
for x in range(min(a,b),0,-1):
    if a%x ==0 and b%x == 0:
        print(x)
        break