T = int(input())
for i in range(T):
    n, m = map(int,input().split()) #m의 이진수 표현의 마지막 n비트

    m_bin = list(bin(m))[2:] #bin()함수로 m을 이진수로 만들어주고, 앞의 0b를 빼줌

    for x in range(len(m_bin)-n,len(m_bin)): #2진수의 마지막 n비트를 비교했을 때
        if len(m_bin) < n: #2진수의 길이가 n보다 짧으면 무조건 0이 들어감
            print('#{} {}'.format(i+1,'OFF')) #그래서 OFF 출력
            break
        elif m_bin[x] == '0': #그렇지 않을 때, n비트를 비교했을 때 0이 들어있다면 
            print('#{} {}'.format(i+1,'OFF')) #OFF 출력
            break
    else:
        print('#{} {}'.format(i+1,'ON')) #아니라면 ON 출력
    