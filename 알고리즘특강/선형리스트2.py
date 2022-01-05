#데이터 삽입 : 중간에 삽입
##함수
def add_data(friend): #선형 리스트에 빈 칸 추가하는 함수
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend): #중간에 데이터를 삽입하는 함수
    katok.append(None) #빈칸을 만들어 준 다음
    kLen = len(katok)
    for i in range(kLen-1, position, -1): #position(원하는 위치)에 데이터가 갈 때 까지 반복
        katok[i] = katok[i-1] #데이터를 한 칸씩 뒷자리로 옮기고,
        katok[i-1] = None #원래 자리는 빈칸으로 만듬
    katok[position] = friend #원하는 위치까지 도착했으면 그 빈칸에 friend(원하는) 데이터 삽입

##전역변수
katok = [] #선형 리스트

##메인코드
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

insert_data(3, '미나')
print(katok)
insert_data(5,'유정')
print(katok)