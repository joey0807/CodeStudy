n, m = map(int, input().split())
nList, mList, ans = [], [], []
count = 0

for i in range(n):
    name = input()
    nList.append(name)

for j in range(m):
    name = input()
    mList.append(name)
#두 리스트의 교집합을 구하는 방법 : set(a) & set(b)
ans = sorted(list(set(nList) & set(mList))) #nList와 mList의 교집합을 정렬된 list 형태로 저장

print(len(ans))
for x in ans:
    print(x)