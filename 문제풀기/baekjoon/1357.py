a, b = input().split()

rev_a = a[::-1] #a의 모든 자리수 역전
rev_b = b[::-1] #b의 모든 자리수 역전

ans = int(rev_a) + int(rev_b) #역전한 값들을 더한 값

print(int(str(ans)[::-1])) #ans값의 모든 자리수를 역전한 값 출력