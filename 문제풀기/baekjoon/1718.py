s = input()
key = input()
ans = ''

for x in range(len(s)):
    if s[x] == ' ':
        ans += ' '
        continue
    d = ord(s[x]) - ord(key[x%len(key)])
    if d > 0:
        ans += chr(d+96)
    else:
        ans += chr(d+26+96)

print(ans)