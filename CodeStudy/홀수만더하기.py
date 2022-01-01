#2072
T = int(input()) #테스트 케이스 개수 T 입력받음

for i in range(T): #테스트 케이스만큼 반복
  arr = list(map(int,input().split())) #입력 받은 수들을 리스트에 저장
  #list comprehension -> 수학적으로 집합을 정의하는 방법
  #입력받은 수 중에서 홀수만 더한 값을 출력하는 문제이므로
  #2로 나눴을 때 나머지가 1인 값들만 ans에 저장
  ans = [num for num in arr if num%2 ==1] 
                           
  print("#{} {}".format(i+1,sum(ans))) #sum으로 홀수들을 더한 후 출력