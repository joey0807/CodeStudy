import sys
sys.setrecursionlimit(10**7) #재귀함수 한도 늘려주는 함수

def A(x,n):
    global m #m 가져오기
    if x <= n: #x가 n보다 작거나 같으면
        m += x #m값에 x 추가
        A(x+1,n) #x++

n = int(input())
m = 0 #합을 저장할 변수
A(1,n)

print(m)