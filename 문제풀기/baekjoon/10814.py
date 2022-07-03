n = int(input())
customer = []

for x in range(n):
    age, name = input().split()
    customer.append((int(age), name))

sort_customer = sorted(customer, key=lambda x : x[0])

for y in range(n):
    print(*sort_customer[y])
