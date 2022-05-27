import sys #입력데이터가 많은 문제는 sys 라이브러리의 readline() 함수 이용하면 시간초과를 피할 수 있다

#하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()

#입력받은 문자열 그대로 출력
print(input_data)