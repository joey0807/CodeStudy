n = int(input())

#n_list = list(map(int,str(n)))
for x in range(1,n):
    x_list = list(map(int, str(x)))
    if x+sum(x_list) == n:
        print(x)
        break
else:
    print(0) #조건에 맞는 생성자가 없으면 0 출력