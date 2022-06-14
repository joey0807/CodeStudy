while True:
    try: #여러 개의 테스트 케이스로 이루어지므로 try-except
        a,b,c = map(int, input().split())

        ans = max(b-a,c-b) #b-a와 c-b중 더 큰 값 구하기
        print(ans-1) #구한값-1이 정답
    except:
        break