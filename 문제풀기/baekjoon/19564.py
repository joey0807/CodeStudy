s = input()
keyboard = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k = 1

for x in range(len(s)-1):
    if keyboard.index(s[x]) < keyboard.index(s[x+1]):
        continue
    else:
        k += 1

print(k)