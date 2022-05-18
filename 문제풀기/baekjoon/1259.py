while True:
    n = input()

    if n == '0': #숫자 0을 입력하면
        break #함수 종료

    if n == n[::-1]: #숫자와 펠린드롬수가 같다면
        print('yes') #yes 출력
    else: #아니면
        print('no') #no 출력

