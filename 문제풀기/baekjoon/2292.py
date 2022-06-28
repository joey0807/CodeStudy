# n = int(input()) -> 메모리 초과
# bee = [1]
# count = 0
# for x in range(1,n//3):
#     bee.append(x*6)

# for x in range(n):
#     if n > count:
#         count += bee[x]

#     else:
#         print(x)
#         break

n = int(input())
bee = 1
count = 1

while n > bee:
    bee += count * 6
    count += 1

print(count)