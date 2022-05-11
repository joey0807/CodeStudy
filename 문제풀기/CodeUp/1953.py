def A(x,y):
    if x <= y: #x가 y와 같아질 때 까지
        print('*'*x) #* 하나씩 늘려가며 출력
        A(x+1,y)

n = int(input())
A(1,n) #* 1개부터 시작