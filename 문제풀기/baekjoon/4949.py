while True:

    n = input()
    ans = []

    if n == '.':
        break

    for x in n:
        if x == '(' or x == '[':
            ans.append(x)

        elif x == ')':
            if ans and ans[-1] == '(': #ans 리스트 안에 값이 있고 마지막 값이 ( 라면 삭제
                ans.pop()

            else:
                print('no')
                break

        elif x == ']':
            if ans and ans[-1] == '[': #ans 리스트 안에 값이 있고 마지막 값이 [ 라면 삭제
                ans.pop()
                
            else:
                print('no')
                break

    else:
        if not ans:
            print('yes')
        else:
            print('no')