T = int(input())

for i in range(T):
  P, Q, R, S, W = map(int,input().split()) #P(A사 1리터당 P원)/Q(B사 기본요금Q원)/R(B사 R리터 이하일때만 기본요금)/S(R리터 초과했을때 리터당 S원)/W(한달간 사용하는 리터 양)
  
  CompanyA = P * W #A사의 계산방식
  CompanyB = 0 #리터에 따라 계산방법이 다름
  result = 0 #결과값

  if (W-R)>0: #한달에 사용한 수도 양이 기본 사용량보다 많을때
    CompanyB = Q+S*(W-R)
  if(W-R)<0: #한달에 사용한 수도 양이 기본 사용량보다 적을때
    CompanyB = Q
  
  if(CompanyA < CompanyB): #두 회사의 계산값을 비교해서 작은 값 출력
    result = CompanyA
  else:
    result = CompanyB

  print('#{} {}'.format(i+1,result))
