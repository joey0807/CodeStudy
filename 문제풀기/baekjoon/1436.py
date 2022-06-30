n = int(input())
movie = 666
count = 0

while True:
    if '666' in str(movie):
        count += 1
    if count == n:
        print(movie)
        break
    movie += 1