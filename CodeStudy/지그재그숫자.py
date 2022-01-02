#1986
T = int(input()) #테스트케이스 개수 T

for i in range(T): #입력받은 테스트케이스 수만큼 반복
  n = int(input()) #숫자 N 입력받음
  sum = 0 #합을 더할 변수 sum
  for j in range(n+1): #1부터 N까지의 숫자를 계산하기 때문에 반복을 n+1로 설정

    if(j%2==1): #홀수면 더하고
      sum += j

    else: #짝수면 뺀다
      sum -= j

  print("#{} {}".format(i+1,sum)) # 그 결과값 출력