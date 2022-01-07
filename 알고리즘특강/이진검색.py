#이진검색 : 아무리 큰 값이라도 빠르게 찾을 수 있다!
import random

##함수
def binSearch(ary, fData):
  pos = -1
  start = 0
  end = len(ary)-1

  while (start <= end):
    mid = (start + end)//2 #시작과 끝을 더한 값을 나누고 나머지는 버림
    if fData == ary[mid]: #찾는 값이 중간값에 있다면 그대로 리턴
      return mid
    elif fData > ary[mid]: #찾는 값이 중간값보다 크다면
      start = mid+1  #시작값을 중간값+1로 변경
    else: #그 반대로 찾는 값이 중간값보다 작다면
      end = mid -1 #끝값을 중간값-1로 변경

  return pos
##전역
dataAry = [random.randint(1,999) for _ in range(50)]
findData = dataAry[random.randint(0,49)]
dataAry.sort() #데이터 정렬

##메인
print('배열 : ', dataAry)
position = binSearch(dataAry, findData)
if position == -1:
  print(findData, '값이 없음')
else:
  print(findData, '는', position, '위치에 있다')
