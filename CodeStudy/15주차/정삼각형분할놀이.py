T = int(input())
for i in range(T): 
    a, b = map(int, input().split()) #a길이의 정삼각형, b길이의 정삼각형

    ans = a/b #b는 a의 약수니까 나눈 값만큼 개수가 비례

    print('#{} {}'.format(i+1,int(ans**2))) #나눈 값의 제곱 수가 최소 개수