n = int(input()) #개수 n
gas = {} #딕셔너리 형태로 입력받을 것

for i in range(n): #식별번호 a와 가스 보유량 b 입력받고
    a, b = map(int,input().split())
    gas[a] = b #딕셔너리 형태로 저장

sort_gas = sorted(gas.items()) #식별번호를 오름차순으로 정렬해야 하므로 key값을 기준으로 정렬

for x in range(len(sort_gas)):
    print(*sort_gas[x]) #정렬한 딕셔너리를 조건에 맞게 출력