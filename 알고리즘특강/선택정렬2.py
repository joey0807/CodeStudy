#선택정렬 -> 기본(실무)
import random

##함수
def findMinIndex(ary):
  minIdx = 0
  for i in range(1,len(ary)):
    if(ary[minIdx] > ary[i]): 
      minIdx = i
  return minIdx

##전역
before = [random.randint(10,99) for _ in range(20)] #정렬하기 전 배열
after = [] #정렬 후 배열
##메인
print('정렬 전 : ',before)

for i in range(len(before)): #before배열 인덱스 수 만큼 반복
  minPos = findMinIndex(before) 
  after.append(before[minPos]) #findMinIndex() 함수로 정리된 값들을 after 배열에 넣음
  del(before[minPos]) #before배열 값 삭제

print('정렬 후 : ', after)