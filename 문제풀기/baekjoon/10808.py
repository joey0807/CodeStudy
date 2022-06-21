s = input()
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = [0]*26

for x in s:
    for y in range(len(word)):
        if x == word[y]:
            ans[y] += 1

print(*ans)