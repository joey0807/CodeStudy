def process(tp): 
    global password 
    if tp[0] == 'I': #명령어가 I라면
        for x in range(0,len(tp[3:])): #I(삽입) x, y, s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다. s는 덧붙일 숫자들이다.[ ex) I 3 2 123152 487651 ]
            password.insert(int(tp[1])+x, tp[3+x])
    elif tp[0] == 'D': #명령어가 D라면
        for _ in range(int(tp[2])): #D(삭제) x, y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제한다.[ ex) D 4 4 ]
            del password[int(tp[1])]
            if len(password) == int(tp[1]):
                break
    elif tp[0] == 'A': #명령어가 A라면
        for x in range(int(tp[1])): #A(추가) y, s : 암호문의 맨 뒤에 y개의 숫자를 덧붙인다. s는 덧붙일 숫자들이다. [ ex) A 2 421257 796813 ]
            password.append(tp[2+x])

for i in range(10): #테스트케이스 10개
    N = int(input()) #원본 암호문 길이 N
    password = list(input().split()) #원본 암호문 password
    cmdCount = int(input()) #명령어의 개수 cmdCount
    cmd = list(input().split()) #명령어 cmd

    temp = [] #빈 리스트
    cnt = 0 
    for x in cmd: #명령어 리스트문 반복
        if x in ['I','A','D'] and len(temp) > 1: #명령어에 I, A, D가 있고 temp리스트가 비어있지 않다면
            process(temp) #함수 process 실행
            temp = [] #실행 후 temp리스트 초기화
            temp.append(x) #초기화 된 리스트에 명령어 리스트 추가
        else: #아니면
            temp.append(x) #temp 리스트에 명령어 리스트 추가

    print('#{} {}'.format(i+1,' '.join(password[:10])))