#powerset 알고리즘(멱집합)
#어쩐지 어렵더라
#멱집합 : 크기가 n인 모든 부분집합 -> 2^n개

def check(index, total_score, total_cal): #index=현재 리스트들의 인덱스, total_taste=현재 맛에 대한 총 점수, total_cal=현재 총 칼로리
    global ans
    
    if total_cal > L: #총 칼로리(total_cal)가 제한 칼로리(L)보다 크다면
        return #그대로 리턴
    
    if index >= N: #인덱스가 재료의 수(N)보다 크거나 같을 때
        if total_score > ans: #맛에 대한 총 점수(total_score)가 최고 점수(ans)보다 크다면
            ans = total_score #최고 점수 갱신 후 리턴
        return
    #각 재료에 대해서 넣는 경우와 안 넣는 경우를 둘 다 찾음
    check(index+1, total_score + score_taste[index], total_cal + score_calory[index]) #재료를 넣는 경우
    check(index+1, total_score, total_cal) #재료를 넣지 않는 경우
    

T = int(input())
for i in range(T):
    N, L = map(int, input().split()) #N=재료의 수, L=제한 칼로리
    score_taste = [] #맛에 대한 점수를 저장할 리스트
    score_calory = [] #칼로리를 저장할 리스트

    for x in range(N):
        taste, calory = map(int, input().split()) #맛에 대한 점수와 칼로리 입력
        score_taste.append(taste) #리스트에 저장
        score_calory.append(calory)

    ans = 0 #최고 점수
    
    check(0,0,0) #점수를 계산할 함수 check

    print('#{} {}'.format(i+1,ans))
