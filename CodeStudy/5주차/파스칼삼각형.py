T = int(input()) #테스트케이스

for i in range(T):
    N = int(input()) #파스칼 삼각형 크기 N 입력

    pascal = [[1],[1,1]] #파스칼 삼각형의 처음 2개
    for x in range(2,N): #3번째 줄부터 파스칼 삼각형을 나타내는 법
        pascal_list = [1] #첫번째 숫자는 1
        for y in range(x-1): #사잇값 계산
            pascal_list += [pascal[x-1][y] + pascal[x-1][y+1]]
        
        pascal_list += [1] #마지막 숫자도 1
        pascal += [pascal_list] #계산한 사잇값 더하기

    print('#{}'.format(i+1))
    for z in range(N):
        print(*pascal[z]) #계산된 파스칼 삼각형을 글자 단위로 출력
