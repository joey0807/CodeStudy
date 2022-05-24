#'재귀함수를 호출합니다' 문자열을 무한히 출력
# def recursive_function():
    # print('재귀함수를 호출합니다')
    # recursive_function()
# 
# recursive_function()

#재귀함수 종료 예제
# def recursive_function(i):
    #100번째 출력했을 때 종료되도록 종료 조건 명시
    # if i == 100:
        # return
    # print(i,'번째 재귀 함수에서',i+1,'번째 재귀 함수를 호출합니다.')
    # recursive_function(i+1)
    # print(i, '번째 재귀 함수를 종료합니다.')
# 
# recursive_function(1)

#2가지 방법으로 구현한 팩토리얼 예제

#반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1,n+1):
        result *= i

    return result

#재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: #n이 1 이하인 경우 1을 반환
        return 1
    
    #n! = n*(n-1)!를 그대로 코드로 작성 
    return n * factorial_recursive(n-1)

print('반복적으로 구현 : ',factorial_iterative(5))
print('재귀적으로 구현 : ',factorial_recursive(5))