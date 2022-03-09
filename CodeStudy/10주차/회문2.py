for i in range(10):
    T = int(input())
    palindrom = []
    for _ in range(100):
        palindrom.append(input())

    def pld(string, length):
        max = length
        while(length <= 100):
            answer = 0
            for x in range(100):
                for y in range(101-length):
                    word = string[x][y:y+length]
                    if word == word[::-1]:
                        max = length
                        answer = 1
                        break
                if answer == 1:
                    break
            length += 1
        return max

    # 가로줄
    row = pld(palindrom, 1)

    # 세로줄
    palindrom2 = []
    for x in range(100):
        list = ""
        for y in range(100):
            list += palindrom[y][x]
        palindrom2.append(list)

    col = pld(palindrom2, 1)

    print("#{} {}".format(T, max(row, col)))