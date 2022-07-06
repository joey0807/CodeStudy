t = int(input())
for i in range(t):
    ps = input()
    vps = []
    count = 0
    
    for x in ps:
        if x == '(':
            vps.append(x)
        elif x == ')':
            if vps: #vps 리스트에 값이 괄호가 있으면 삭제, 없으면 vps가 아니니 no 출력
                vps.pop()
            else:
                print('NO')
                break
    else:
        if not vps:
            print('YES')
        else:
            print('NO')
