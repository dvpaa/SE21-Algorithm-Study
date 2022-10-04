N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)
s = 0

for x, y in zip(A, B):
    s += (x * y)
print(s)
