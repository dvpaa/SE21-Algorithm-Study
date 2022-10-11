n = int(input())
point = []

for i in range(n):
    point.append(list(map(int, input().split())))


for i in sorted(point):
    print(i[0], i[1])
