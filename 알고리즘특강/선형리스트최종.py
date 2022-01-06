##함수
def add_data(friend): #선형리스트에 빈 칸을 추가하는 함수
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend): #선형리스트 중간에 데이터를 삽입하는 함수
    katok.append(None)
    kLen = len(katok)
    for i in range(kLen-1, position, -1) :
        katok[i] = katok[i-1]
        katok[i-1] = None
    katok[position] = friend

def delete_data(position):
    katok[position] = None #position(원하는 위치)의 데이터 삭제(None)
    kLen = len(katok) 
    for i in range(position+1, kLen, 1): #position의 다음 칸부터 katok 리스트 끝까지 반복
        katok[i-1] = katok[i] #한칸씩 당겨서 값 채워넣기
        katok[i] = None #당겨진 칸은 빈칸으로 만들어주기

    del(katok[kLen-1]) #배열 맨 마지막 위치를 완전히 제거

##전역변수
katok = []
select = -1 #선택 숫자를 입력받는 변수

##메인
if __name__ == '__main__':

    while(select != 4):
        select = int(input('선택하세요(1:추가, 2:삽입, 3:삭제, 4:종료)-->'))

        if(select == 1):
            data = input('추가할 데이터-->') #데이터 추가
            add_data(data)
            print(katok)

        elif(select == 2):
            pos = int(input('삽입할 위치-->')) #원하는 위치에 데이터 삽입
            data = input('추가할 데이터-->')
            insert_data(pos, data)
            print(katok)

        elif(select == 3):
            pos = int(input('삭제할 위치-->')) #데이터 삭제
            delete_data(pos)
            print(katok)

        elif(select == 4): #실행 종료
            print(katok)
            exit
        else:
            print('1~4중 하나를 입력하세요')
            continue