T = int(input()) #테스트케이스
for i in range(T):
    memory = list(input()) #메모리 원래 값
    origin_memory = ['0' for _ in range(len(memory))] #초기화 상태의 메모리값
    num = 0 #숫자 카운팅 변수

    for x in range(len(memory)): #메모리 길이 만큼 반복
        if memory[x] != origin_memory[x]: #초기화 상태의 메모리값과 원래 값과 다르다면
            for y in range(x, len(memory)): #그 다음 값부터 끝까지의 값들이
                origin_memory[y] = memory[x] #다른 메모리 값으로 전부 바뀜
            num += 1 #바뀐 숫자 카운팅
            
    print('#{} {}'.format(i+1,num))
