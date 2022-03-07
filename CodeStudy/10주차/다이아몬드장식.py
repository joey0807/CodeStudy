T = int(input()) #테스트케이스 개수

for i in range(T):
    word = input() #입력할 문자열
    num = len(word) #문자열 개수

    answer = ['']*5 #총 5줄

    answer[0] += '..#.'*num + '.' #첫 번째 줄 규칙
    answer[1] += '.#.#'*num + '.' #두 번째 줄 규칙
    for x in word: #세 번째 줄 규칙
        answer[2] += '#.' + x  + '.' #사이에 문자열 하나씩 끼워넣기
    answer[2] += '#' #마지막은 #으로
    answer[3] += '.#.#'*num + '.' #네 번째 줄 규칙
    answer[4] += '..#.'*num + '.' #다섯 번째 줄 규칙

    for y in answer: #장식된 문자열 출력
        print(y)