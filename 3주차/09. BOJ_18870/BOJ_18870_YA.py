N = int(input())
x = list(map(int, input().split()))
y = []
for i, value in enumerate(x):
    y.append([i, value])
y.sort(key=lambda k: k[1])
a = 0
y[0].append(0)
for i in range(1, len(y)):
    if y[i-1][1] == y[i][1]:
        a += 1
    y[i].append(i - a)
y.sort(key=lambda k: k[0])
for i in y:
    print(i[2], end=' ')

# for i in range(len(y)):
#     y[i][1] = i
# y.sort(key=lambda a: a[0])
# for i in y:
#     print(i[1], end=' ')
