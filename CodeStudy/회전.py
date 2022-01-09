#회전

T = int(input()) #테스트 케이스 개수 T

for i in range(T): #T만큼 반복
  n, m = map(int, input().split()) #n:배열 칸 개수/m:맨 앞의 숫자를 맨 뒤로 보내는 작업 반복수
  queue = input().split() #공백을 기준으로 숫자를 입력받음
  #n번 반복하면 원상태이므로 m을 n으로 나눈 나머지 숫자의 배열이 출력되는 값
  m %= n
  print('#{} {}'.format(i+1, queue[m]))