s = input()
word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ans = [-1]*26
count = 1

for x in s:
    for y in range(len(word)):
        if x == word[y]:
            if ans[y] == -1:
                ans[y] += count
                count += 1
            else:
                count += 1

print(*ans)