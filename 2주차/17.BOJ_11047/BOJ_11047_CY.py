n, k = map(int, input().split())
a = []
cs = 0
for _ in range(n):
    a.append(int(input()))

for i in range(n-1,-1,-1):
    cs += k // a[i]
    k %= a[i]

print(cs)