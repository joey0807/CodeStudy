n = int(input())

while True:
    bool = True #참거짓 유무 변수
    for x in str(n): #숫자 n을 문자열로 바꿔서 하나씩 비교
        if x != '4' and x != '7': #4나 7이 아니면
            bool = False #bool은 False로 바꿔주고
            n -= 1 #n 1 감소

    if bool: #맞다면 출력 후 정지
        print(n)
        break