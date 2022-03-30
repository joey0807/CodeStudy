T = int(input())

#백트레킹을 쓴다더라..
#임의의 집합에서 기준에 따라 원소의 순서를 선택

#유망의 조건1 : 같은 열 체크
#col[i] : i번째 행에서 퀸이 놓여있는 열의 위치
#col[k] : k번째 행에서 퀸이 놓여있는 열의 위치
#col[i] == col[k] : 같은 행이므로 유망x

#유망의 조건2 : 대각선 체크
#왼쪽 대각선 : 열에서의 차이는 행에서의 차이와 같다
#             col[i] = col[k] == i - k
#오른쪽 대각선 : 열에서의 차이는 행에서의 차이의 음수와 같다
#               col[i] - col[k] == k - i
#col[i]와 col[k]의 절대값으로 대각선 판단

def n_queens(col,i): #행을 바꾸면서 내려가는 함수
    global ans
    n = len(col) - 1
    if (promissing(col,i)): #조건 확인 함수가 True라서 조건이 맞을 때
        if (i==n): #끝까지 도달했다면
            ans += 1 #정답 개수 +1
        else: #정답이 아니라면
            for j in range(1,n+1): #1부터 n까지 확인
                col[i+1] = j #각각의 위치에 퀸을 놔두고
                n_queens(col, i+1) #재귀함수로 반복

def promissing(col,i): #조건 확인 함수
    k = 1
    flag = True
    while (k<i and flag): #k가 i보다 작고 flag가 True일 때
        if (col[i] == col[k] or abs(col[i]-col[k]) == (i-k)): #같은 열에 있거나, 또는 같은 대각선에 있으면 
            flag = False #정답이 아니니까 False
        k += 1 #조건에 안걸리면 True
    return flag

for i in range(T):
    n = int(input()) 
    ans = 0
    col = [0]*(n+1)
    n_queens(col, 0)


# def queen(x):
#     global ans

#     if x == N: #마지막행까지 다 놓았다면 함수 종료
#         ans += 1 
#         return

#     for y in range(N):
#         if (y in columns) or (x+y in l_diagonal) or (x-y in r_diagonal): 
#             continue #계속 반복
#         columns.add(y)
#         l_diagonal.add(x+y)
#         r_diagonal.add(x-y)
#         queen(x+1)
#         columns.remove(y)
#         l_diagonal.remove(x+y)
#         r_diagonal.remove(x-y)

# for i in range(T):
#     N = int(input())

#     ans = 0 #정답 개수
#     columns, l_diagonal, r_diagonal = set(), set(), set() 

#     queen(0)

    print('#{} {}'.format(i+1,ans))
    