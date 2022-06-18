n = int(input())
dragon = list(map(int, input().split()))
mountain = dragon[0]
sum = 0
ans = []

for x in range(1,len(dragon)):
    if mountain > dragon[x]:
        sum += 1
        #print("mountain : ",mountain, "sum : ",sum)

    else:
        #ans.append(sum)
        sum = 0
        mountain = dragon[x]
        #print("mountain : ",mountain, "sum : ",sum)

    ans.append(sum)

#print(ans)
print(max(ans))