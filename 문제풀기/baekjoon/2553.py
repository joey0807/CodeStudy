import math

n = int(input())

# def factorial(x):
    # while x <= 1:
        # return 1
    # return x*factorial(x-1)

f = str(math.factorial(n)) #재귀함수보다 math 라이브러리가 훨씬 빠르네

for x in f[::-1]:
    if x == '0':
        continue
    else:
        print(x)
        break
        