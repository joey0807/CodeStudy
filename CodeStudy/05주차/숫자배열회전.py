T = int(input()) #테스트케이스

for i in range(T):
    N = int(input()) #배열 길이

    array = [list(map(int,input().split())) for _ in range(N)] #배열 입력
    ans = [] #결과로 나오는 배열

    for x in range(N): #90도 회전
        number = '' #문자열 형태로 회전한 값 저장
        for y in range(N-1,-1,-1): 
            number += str(array[y][x]) #회전해서 나온 값을 문자열로 저장
        ans.append(number+' ') #ans 배열에 append로 저장

    for x in range(N-1,-1,-1): #180도 회전
        number = ''
        for y in range(N-1,-1,-1):
            number += str(array[x][y])
        ans.append(number+' ')

    for x in range(N-1,-1,-1): #270도 회전
        number = ''
        for y in range(N):
            number += str(array[y][x])
        ans.append(number)

    print('#{}'.format(i+1))
   
    for x in range(N): #결과로 나오는 배열 출력
        for y in range(0,len(ans),N):
           print(ans[x+y],end='')
        print()