for i in range(10):
    N = int(input())
    inputString = input()
    testString = input()
    num = 0


    for x in range (len(testString)):
        if testString[x] == inputString[0]:
            if testString[x:x+len(inputString)] == inputString:
                num += 1

    #print('#{} {}'.format(N,testString.count(inputString)))
    #개사기 count()함수를 왜 몰랐지!
                
    print('#{} {}'.format(N,num))
