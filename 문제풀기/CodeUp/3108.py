n=int(input()) #입력 데이터 개수
data=[] #수험 번호와 이름을 저장할 리스트
no_list=[] #수험 번호를 저장할 리스트

for i in range(n):
    c,no,name=input().split() #데이터 개수만큼 코드, 수험 번호, 이름 입력받음

    if c == "I": #코드가 I 일 때
        if int(no) not in no_list: #no_list에 수험번호가 없다면 
            no_list.append(int(no)) #no_list에 수험번호 추가
            data.append([int(no),name]) #data에도 수험번호와 이름 추가

    elif c == "D": #코드가 D 일 때
        if int(no) in no_list: #수험번호가 no_list에 있다면
            no_list.remove(int(no)) #no_list에 있는 수험번호 삭제
            for j in range(len(data)): #data 리스트 안에 있는 수험번호들을 다 지워야 하니까 반복문
                if data[j][0]==int(no): #수험번호가 같은 것들이 있으면
                    del data[j] #삭제
                    break 
        
print_list = list(map(int,input().split())) #5개 숫자 입력받고

sort_data = sorted(data, key=lambda x:x[0]) #정리한 data 리스트들을 수험번호에 맞게 정렬

for i in range(len(print_list)):
    print(sort_data[print_list[i]-1][0],sort_data[print_list[i]-1][1]) #입력 받은 숫자에 맞는 위치의 data 정보 출력