import sys
input = sys.stdin.readline

n = int(input())
xPoint = list(map(int, input().split()))
xPoint2 = sorted(set(xPoint))

a = dict()
for idx, val in enumerate(xPoint2):
    a[val] = idx

for i in xPoint:
    print(a[i], end=' ')
