n = int(input())
stack = [] #숫자들을 저장할 리스트
ans = [] #계산에 맞게 +, - 를 저장할 리스트
count = 1 #오름차순으로 스택에 push -> 1부터 시작

for _ in range(n):
    x = int(input()) #숫자 입력
    while count <= x: #입력한 숫자에 도달할 때 까지 1부터 차례대로 stack에 push
        stack.append(count)
        ans.append('+') #push 했으니 + 저장
        count += 1

    if stack[-1] == x: #stack의 마지막 값이 입력받은 숫자 x와 같아지면
        stack.pop() #stack의 마지막 값을 꺼냄
        ans.append('-') #꺼내니까 - 저장

    else: #stack의 마지막 값이 입력받은 숫자가 아니라면 주어진 스택을 만들 수 없음
        print('NO') #오름차순으로 스택이 입력되는데 마지막 값이 x보다 크면 x는 마지막 값보다 더 아래에 있기 때문
        break #NO 출력 후 종료

else: #다 연산이 완료되었다면
    for i in range(len(ans)):
        print(ans[i]) #연산 기호 출력