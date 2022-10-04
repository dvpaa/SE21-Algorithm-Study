n = int(input())
p = sorted(list(map(int, input().split())))
s = 0
for i in range(n):
    s += p[i] * (n - i)
print(s)
