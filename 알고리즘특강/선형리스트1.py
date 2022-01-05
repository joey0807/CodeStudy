#데이터 삽입 : 끝에 삽입
##함수
def add_data(friend): #선형 리스트에 추가
    katok.append(None) #append() : 리스트 형태의 data 마지막에 하나를 추가하는 함수, 선형 리스트에 빈칸을 추가
    kLen = len(katok) #katok 리스트 길이
    katok[kLen-1] = friend #katok 리스트 마지막에 데이터 friend 삽입

##전역변수
katok = [] #선형 리스트

##메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

add_data('모모') #추가한 빈 칸에 데이터 추가
print(katok)