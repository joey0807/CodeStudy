n = int(input())
array = []

#n개의 정수를 입력받아 리스트에 저장
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True) #파이썬 기본 정렬 라이브러리를 이용해 정렬 수행

for i in array:
    print(i,end=' ')