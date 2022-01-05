#데이터 삭제 : 중간 삭제
##함수
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
    katok[position] = None #position(원하는 위치)의 데이터 삭제(None)
    kLen = len(katok) 
    for i in range(position+1, kLen, 1): #position의 다음 칸부터 katok 리스트 끝까지 반복
        katok[i-1] = katok[i] #한칸씩 당겨서 값 채워넣기
        katok[i] = None #당겨진 칸은 빈칸으로 만들어주기

    del(katok[kLen-1]) #배열 맨 마지막 위치를 완전히 제거
##전역변수
katok = []

##메인코드
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)
delete_data(4)
print(katok)