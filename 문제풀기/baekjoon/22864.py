a,b,c,m = map(int, input().split()) #한 시간 단위로 a:쌓이는 피로도, b:처리한 일의 양, c:줄어드는 피로도, m:피로도 한계치
work, sleep = 0, 0 #일의 총합 work, 피로도 sleep

if a > m: #쌓이는 피로도가 한계치를 넘으면
    print(0) #일 못하니까 0
else:
    for i in range(24): #24시간동안 일
        if sleep + a <= m: #1시간 일을 했을 때 피로도 한계치를 안넘었다면
            work += b #b만큼 일한 양 추가
            sleep += a #a만큼 피로도 추가
        else: #한계치를 넘어간다면 쉬어야 함
            if sleep - c > 0: #현재 피로도에서 c를 뺐을 때 0보다 크면
                sleep -= c #그냥 빼주고
            else: #음수가 된다면
                sleep = 0 #0으로 바뀜

    print(work) #최종적으로 일한 양 출력
