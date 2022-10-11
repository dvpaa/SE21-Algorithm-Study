num = list(map(int, input()))

num.sort(reverse=True)
for i in num:
    print(i, end='')