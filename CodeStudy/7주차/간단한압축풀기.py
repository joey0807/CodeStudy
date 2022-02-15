T = int(input()) #테스트케이스
for i in range(T):
    N = int(input()) #입력할 알파벳과 숫자 쌍 개수
    file = [] #알파벳을 저장할 리스트

    for x in range(N): #알파벳과 숫자 입력받기
        alphabet, number = input().split()
        number = int(number)

        file += [alphabet for a in range(number)] #입력받은 알파벳 저장
    
    print('#{}'.format(i+1))

    for y in range(len(file)): #파일 길이 맞춰주기
        if (y+1)%10 == 0: #행의 개수가 10개가 되면
            print(file[y]) #출력하고 밑의 print()로 줄변환
        else: #10개 안됐으면
            print(file[y], end='') #공백없이 계속출력
    print()



        