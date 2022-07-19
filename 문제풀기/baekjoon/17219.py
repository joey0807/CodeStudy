n, m = map(int, input().split())
data = {}

for i in range(n):
    ad, pw = input().split()
    data[ad] = pw

for j in range(m):
    ad = input()
    print(data[ad])