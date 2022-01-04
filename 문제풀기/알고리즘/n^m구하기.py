#임의의 정수 n, m이 주어졌을 때 n^m을 구하는 함수 작성
#**연산자를 사용하지 않기

def power(a,b):
    sum = 1
    for i in range(b):
        sum *= n
    
    return sum

n, m = map(int, input().split())
print(power(n,m))