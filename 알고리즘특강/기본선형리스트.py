def add_data(friend): #선형 리스트에 빈 칸 추가하는 함수
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def  insert_data(position, friend) : #선형 리스트 중간에 데이터를 삽입하는 함수
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position): #선형 리스트 중간의 데이터를 삭제하는 함수
    katok[position] = None 
    kLen = len(katok) 
    for i in range(position+1, kLen, 1): 
        katok[i-1] = katok[i] 
        katok[i] = None 

    del(katok[kLen-1])

katok = []
select = -1 #while문 반복을 위해 기본값을 -1로 설정

if __name__ == "__main__": #모듈에 이 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것
                           #직접 호출되어 사용될 때는 그 자체로 기능을 수행하고, 동시에 다른 모듈에서 필요한 함수 등을 제공할 수 있다

  while(select != 4):
    select = int(input('선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료)-->')) #입력할 숫자에 따라 다르게 실행

    if(select == 1): #데이터 추가
      data = input('추가할 데이터-->')
      add_data(data)
      print(katok)

    elif(select == 2): #데이터 삽입
      pos = int(input('삽입할 위치-->'))
      data = input('추가할 데이터-->')
      insert_data(pos, data) #원하는 위치, 원하는 데이터
      print(katok)

    elif(select == 3): #데이터 삭제
      pos = int(input('삭제할 위치-->'))
      delete_data(pos) #삭제할 위치
      print(katok)

    elif(select == 4): #종료
      print(katok)
      exit #최종 선형 리스트를 출력하면서 종료
    else:
      print('1~4중 하나를 입력하세요') #1~4 외에 다른 숫자를 입력했을 때 나오는 문장
      continue #문장 출력 후 다시 반복
