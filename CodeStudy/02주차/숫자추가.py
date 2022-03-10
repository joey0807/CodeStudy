#숫자추가(스택 or 연결리스트)
T = int(input()) #테스트케이스 개수 T
 
for i in range(T): #T만큼 반복
  N, M, L = map(int, input().split()) #N:수열길이, M:추가횟수,L:출력할 인덱스 번호
  lst = list(map(int,input().split())) #공백을 기준으로 배열 입력
  
  for j in range(M): #숫자 추가 횟수만큼 반복
    a, b = map(int, input().split()) #공백을 기준으로 a(인덱스번호),b(추가하려는 숫자) 입력
    lst.append(None) #배열 끝에 빈 칸 추가
    lstLen = len(lst) #배열 길이 측정
    for k in range(lstLen-1,a,-1): #중간에 값을 넣기 위한 반복문
      lst[k] = lst[k-1] #한칸씩 뒤로 당기고
      lst[k-1] = None #뒤로 당긴 칸을 비운 다음
    lst[a] = b #원하는 인덱스까지 반복해서 왔으면 빈 칸에 추가하려는 숫자 추가

  print('#{} {}'.format(i+1,lst[L]))