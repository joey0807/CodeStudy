n = input() #점수 n 입력

left = n[:int(len(n)/2)] #n을 반으로 나눴을 때 왼쪽 값
right = n[int(len(n)/2):] #n을 반으로 나눴을 때 오른쪽 값

sum1, sum2 = 0, 0

for x in left:
    sum1 += int(x) #왼쪽 값 모두 더하기

for y in right:
    sum2 += int(y) #오른쪽 값 모두 더하기

if sum1 == sum2: #두 값이 같다면 lucky, 다르다면 ready
    print('LUCKY')
else:
    print('READY')