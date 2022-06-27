a, b = input().split()

l_a = a[::-1]
l_b = b[::-1]

if int(l_a) < int(l_b):
    print(l_b)
else:
    print(l_a)

