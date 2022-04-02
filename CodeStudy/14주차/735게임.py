T = int(input())
for i in range(T):
    game = list(map(int, input().split())) #서로 다른 7개의 정수 입력
    lst = [] #3개의 정수를 골라 합한 숫자들을 저장할 리스트

    for x in range(5): #첫번째 숫자는 game[0]부터 game[4]까지
        for y in range(1,6): #두번째 숫자는 game[1]부터 game[5]까지
            for z in range(2,7): #세번째 숫자는 game[2]부터 game[6]까지
                if x!=y and y!=z and x!=z: #같은 숫자를 중복으로 더하면 안되니까 예외처리
                    lst.append(game[x]+game[y]+game[z]) #세 숫자의 합을 lst에 저장

    set_lst = list(set(lst)) #만들어진 lst의 중복값을 제거하고
    set_lst.sort(reverse=True) #내림차순으로 바꿔줌
    
    print('#{} {}'.format(i+1,set_lst[4])) #5번째로 큰 수니까 set_list의 5번째 숫자 출력



