T = int(input()) #테스트케이스 개수
for i in range(T):
    N, length = input().split() #N=테스트케이스 번호, length=입력받을 문자열 길이
    testcase = list(input().split()) #입력받을 문자열

    number = ("ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN") 

    new_testcase = [] #정렬을 위한 빈 문자열
    for x in range(int(length)): 
        new_testcase.append(number.index(testcase[x])) #문자의 인덱스 번호가 그 문자의 숫자를 나타냄 -> 인덱스 번호를 new_testcase에 저장

    new_testcase.sort() #저장된 인덱스 번호들을 정렬

    for y in range(int(length)): 
        new_testcase[y] = number[new_testcase[y]] #정렬된 인덱스 번호들을 다시 문자열로 바꿈

    print("{}".format(N))
    print(*new_testcase) #바뀐 문자열 출력