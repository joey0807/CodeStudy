T = int(input()) #테스트케이스

for i in range(T):
    sudoku = [list(map(int,input().split()))for _ in range(9)] #스도쿠 입력
    check = 1 #스도쿠 확인 변수 => 맞으면 1, 틀리면 0
    One2Nine = set(range(1,10)) #1부터 9까지 있는지 확인하는 용도

    #3줄씩 묶어서 비교
    zip_sudoku = list(map(list, zip(*sudoku))) #스도쿠 세로줄, zip 함수로 세로줄을 가로줄로 반전시켜 입력받음
    for x in range(3):
        for y in range(3):
            if set(sudoku[x*3:x*3+3][0:3][y]) != One2Nine or set(zip_sudoku[x*3:x*3+3][0:3][y]) != One2Nine: #1부터 9까지의 숫자가 포함돼있지 않으면
                check = 0 #틀린 것이므로 0 출력

    for x in range(0,9,3): #3x3 확인
        for y in range(3):
            box = [] #비교하기 위해 입력받을 리스트
            for z in range(3):
                box += sudoku[x+z][y*3:y*3+3] #빈 리스트에 3x3 숫자를 입력받음

            if set(box) != One2Nine: #조건을 만족하지 않으면
                check = 0 #0 출력

    print('#{} {}'.format(i+1,check))