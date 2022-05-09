def A(n):
    if n == 1: #n이 1이 되면 과정이 끝났으니 리턴
        return
    elif n%2 == 1: #n이 홀수라면
        n = n*3 + 1 #3n+1
        ans.append(n) #ans에 값 저장
        A(n) #다시 우박수 함수 반복
    elif n%2 == 0: #n이 짝수라면
        n /= 2 #2로 나누기
        ans.append(n) #ans에 값 저장
        A(n) #다시 우박수 함수 반복

def B(x,y):
    if y > 0: #y가 0이 될 때 까지 반복
        print(int(x[y-1])) #x리스트 값을 역순으로 출력하는 것을 반복
        B(x,y-1)


n = int(input())
ans = [] #과정 값들을 저장할 리스트
A(n)
B(ans,len(ans))
print(n)