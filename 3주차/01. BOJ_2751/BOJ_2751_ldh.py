import sys
input = sys.stdin.readline

n = int(input().rstrip())
p = []

for i in range(0, n):
    p.append(int(input().rstrip()))

p.sort()

for i in p:
    print(i)
