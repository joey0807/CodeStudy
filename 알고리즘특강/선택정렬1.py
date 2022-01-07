#선택 정렬
import random #랜덤 함수

##함수
def findMinIndex(ary):
  minIdx = 0
  for i in range(1,len(ary)):
    if(ary[minIdx] > ary[i]):
      minIdx = i
  return minIdx

##전역
testAry = [random.randint(1,99) for _ in range(20)] #랜덤값

##메인
print(testAry)
minPos = findMinIndex(testAry)
print('최소값 : ', testAry[minPos])